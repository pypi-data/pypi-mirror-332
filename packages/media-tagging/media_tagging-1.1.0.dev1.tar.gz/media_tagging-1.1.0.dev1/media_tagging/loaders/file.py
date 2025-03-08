# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# pylint: disable=C0330, g-bad-import-order, g-multiple-import

"""Loads tagging results from a file."""

import os

import pandas as pd
import pydantic
import smart_open
from typing_extensions import override

from media_tagging import media, tagging_result
from media_tagging.loaders import base


class FileLoaderInput(pydantic.BaseModel):
  """Specifies column names in input file."""

  model_config = pydantic.ConfigDict(extra='ignore')

  identifier_name: str = 'media_url'
  tag_name: str = 'tag'
  score_name: str = 'score'


class FileLoader(base.BaseLoader):
  """Loads tagging results from local or remote file."""

  alias = 'file'

  @override
  def load(
    self,
    media_type: media.MediaTypeEnum | str,
    location: os.PathLike[str] | str,
    **kwargs: str,
  ) -> list[tagging_result.TaggingResult]:
    file_column_input = FileLoaderInput(**kwargs)
    identifier, tag, score = (
      file_column_input.identifier_name,
      file_column_input.tag_name,
      file_column_input.score_name,
    )
    data = pd.read_csv(smart_open.open(location))
    if missing_columns := {identifier, tag, score}.difference(
      set(data.columns)
    ):
      raise base.MediaTaggerLoaderError(
        f'Missing column(s) in {location}: {missing_columns}'
      )
    data['tag'] = data.apply(
      lambda row: tagging_result.Tag(name=row[tag], score=row[score]),
      axis=1,
    )
    grouped = data.groupby(identifier).tag.apply(list).reset_index()
    return [
      tagging_result.TaggingResult(
        identifier=row[identifier],
        type=media_type.name.lower(),
        tagger='loader',
        content=row.tag,
        output='tag',
        tagging_details={'loader_type': self.alias},
      )
      for _, row in grouped.iterrows()
    ]
