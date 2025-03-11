import math
from datetime import datetime
from functools import cached_property
from uuid import UUID
from typing import List, Dict, Optional

import pandas as pd
from pydantic import BaseModel

from talk2data_sdk.database.gene_annotation import GenesAnnotation
from talk2data_sdk.constants import Species, Technology
from talk2data_sdk.constants import BIOTURING_API_USER


class DatabaseInfo(BaseModel):
  """
  Information about the database.
  """
  id: UUID
  tag_name: str
  species: Species
  technology: Technology
  version_id: UUID
  created_time: datetime
  total_cells: int

  def __repr__(self) -> str:
    return (
        "DatabaseInfo("
        f"id={self.id}, "
        f"tag_name={self.tag_name}, "
        f"species={self.species.value}, "
        f"technology={self.technology.value}, "
        f"total_cells={self.total_cells}, "
        f"created_time={self.created_time})"
    )

  def __str__(self):
    return self.__repr__()


class Database:
  """
  A class to interact with the database.
  """

  def __init__(self, connector, info: DatabaseInfo) -> None:
    self._connector = connector
    self._info = info

  # ------------ #
  # Private APIs #
  # ------------ #

  def _post(self, route: str, data: dict) -> dict:
    return self._connector.post(
        route, data, headers={
            "t2d-version": str(self._info.id),
            "btr-user-email": BIOTURING_API_USER,
        }
    )

  def _get_ontology(self, ontology_id: str) -> Dict[str, int]:
    if ontology_id in self._default_project["custom_ontologies"]:
      ontology_id = self._default_project["custom_ontologies"][ontology_id]["id"]
      res = self._post("api/v1/ontology/custom/get", {"id": ontology_id})
    else:
      res = self._post("api/v1/ontology/base/get", {"id": ontology_id})
    return {
        x["label"]: x["id"] for x in res["nodes"]
    }

  def _validate_expression_summary(
      self,
      genes: List[str],
      cell_types: Optional[List[str]],
      tissues: Optional[List[str]],
      conditions: Optional[List[str]],
  ) -> None:
    if not genes:
      raise ValueError("Genes must be provided")
    if len(genes) > 50:
      raise ValueError("Too many genes (at most 50)")
    if not all(self._genes_annotation.is_valid_gene_name(x) for x in genes):
      raise ValueError("Invalid gene(s)")
    if cell_types:
      if len(cell_types) > 50:
        raise ValueError("Too many cell types (at most 50)")
      if not all(x in self.cell_types for x in cell_types):
        raise ValueError("Invalid cell type(s)")
    if tissues:
      if len(tissues) > 50:
        raise ValueError("Too many tissues (at most 50)")
      if not all(x in self.tissues for x in tissues):
        raise ValueError("Invalid tissue(s)")
    if conditions:
      if len(conditions) > 50:
        raise ValueError("Too many conditions (at most 50)")
      if not all(x in self.conditions for x in conditions):
        raise ValueError("Invalid condition(s)")

  def _list_projects(self) -> List[dict]:
    res = self._post("api/v1/project/list", None)
    return res

  def _list_experiments(self, project_id: str) -> List[dict]:
    res = self._post("api/v1/experiment/list", {"project_id": project_id})
    return res

  @cached_property
  def _default_project(self) -> dict:
    return next(x for x in self._list_projects() if x["is_default"])

  @cached_property
  def _default_experiment(self) -> dict:
    return next(
        x for x in self._list_experiments(self._default_project["id"])
        if x["is_default"]
    )

  @cached_property
  def _cell_types(self) -> Dict[str, int]:
    return self._get_ontology("CL")

  @cached_property
  def _tissues(self) -> Dict[str, int]:
    return self._get_ontology("UBERON")

  @cached_property
  def _conditions(self) -> Dict[str, int]:
    return self._get_ontology("MONDO")

  @cached_property
  def _genes_annotation(self) -> GenesAnnotation:
    """
    Get the gene names and aliases.
    """
    res = self._post("api/v1/genes_annotation", None)
    return GenesAnnotation.model_validate(res)

  # ----------- #
  # Public APIs #
  # ----------- #

  @property
  def info(self) -> DatabaseInfo:
    """
    Information about the database.
    """
    return self._info

  @cached_property
  def gene_names(self) -> List[str]:
    """
    The list of gene names of the database.
    """
    return self._genes_annotation.names

  @property
  def tissues(self) -> List[str]:
    """
    The list of tissues in the database.
    """
    return list(self._tissues.keys())

  @property
  def cell_types(self) -> List[str]:
    """
    The list of cell types in the database.
    """
    return list(self._cell_types.keys())

  @property
  def conditions(self) -> List[str]:
    """
    The list of conditions in the database.
    """
    return list(self._conditions.keys())

  def get_expression_summary(
      self,
      genes: List[str],
      *,
      cell_types: Optional[List[str]] = None,
      tissues: Optional[List[str]] = None,
      conditions: Optional[List[str]] = None,
  ) -> pd.DataFrame:
    """
    Get the expression summary of genes in the database.

    Parameters
    ----------
    genes : `List[str]`
      The list of gene names.
    cell_types : `Optional[List[str]]`
      The list of cell types.
    tissues : `Optional[List[str]]`
      The list of tissues.
    conditions : `Optional[List[str]]`
      The list of conditions.

    Returns
    -------
    expression_summary: `pd.DataFrame`
      The expression summary. Columns: `gene`, `cell_type`, `tissue`, `condition`, `sum`,
      `total_cells`, `expressed_cells`, `average`, `coverage`.
    """
    self._validate_expression_summary(genes, cell_types, tissues, conditions)

    cell_types = [self._cell_types[x] for x in cell_types] if cell_types else None
    tissues = [self._tissues[x] for x in tissues] if tissues else None
    conditions = [self._conditions[x] for x in conditions] if conditions else None
    metadata = {"CL": cell_types, "MONDO": conditions, "UBERON": tissues}

    data = {
        "gene_ids": [
            self._genes_annotation.get_gene_id(x) for x in genes
        ],
        "project_id": self._default_project["id"],
        "levels": [
            {
                "experiment_ids": [self._default_experiment["id"]],
                "ontology_id": k,
                "contexts": [
                    {
                        "metadata": {k: v},
                        "genes": {"and_conditions": []}
                    }
                ]
            }
            for k, v in metadata.items() if v is not None
        ],
    }
    res = self._post("api/v1/analysis/heatmap/composition", data)

    expression_summary = []
    for row_data, row_name in zip(res["data"], res["rows"]):
      for data, column_info in zip(row_data, res["columns"]):
        metadata = {
            k: info["node_name"] for k, info in zip(metadata.keys(), column_info)
        }
        expression_summary.append({
            "gene": row_name,
            **metadata,
            "sum": int(math.ceil(data["average"] * data["total_cells"])),
            "total_cells": data["total_cells"],
            "expressed_cells": data["exp_cells"],
            "average": data["average"],
            "coverage": data["exp_cells"] / data["total_cells"] if data["total_cells"] > 0 else 0,
        })

    res = pd.DataFrame(expression_summary)
    res.rename(columns={
        "CL": "cell_type",
        "UBERON": "tissue",
        "MONDO": "condition",
    }, inplace=True)
    return res
