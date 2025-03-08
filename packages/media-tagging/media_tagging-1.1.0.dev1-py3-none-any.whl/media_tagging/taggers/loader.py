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

"""Defines importing tagging results."""

from __future__ import annotations

from typing_extensions import override

from media_tagging import media
from media_tagging.taggers import base


class LoaderTagger(base.BaseTagger):
  """Imports tagging results."""

  alias = 'loader'

  @override
  def create_tagging_strategy(
    self, media_type: media.MediaTypeEnum
  ) -> base.TaggingStrategy:
    raise base.UnsupportedMethodError


class LoaderTaggerError(Exception):
  """Exception for Loader specific taggers."""
