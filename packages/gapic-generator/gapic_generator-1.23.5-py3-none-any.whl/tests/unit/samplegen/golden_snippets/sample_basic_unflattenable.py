# -*- coding: utf-8 -*-
# Copyright 2024 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Generated code. DO NOT EDIT!
#
# Snippet for Classify
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install molluscs-v1-molluscclient


# [START mollusc_classify_sync]
# This snippet has been automatically generated and should be regarded as a
# code template only.
# It will require modifications to work:
# - It may require correct/in-range values for request initialization.
# - It may require specifying regional endpoints when creating the service
#   client as shown in:
#   https://googleapis.dev/python/google-api-core/latest/client_options.html
from molluscs.v1 import molluscclient


def sample_classify(video, location):
    # Create a client
    client = molluscclient.MolluscServiceClient()

    # Initialize request argument(s)
    classify_target = molluscclient.ClassifyTarget()

    # video = "path/to/mollusc/video.mkv"
    with open(video, "rb") as f:
        classify_target.video = f.read()

    # location = "New Zealand"
    classify_target.location_annotation = location

    request = molluscclient.molluscs.v1.ClassifyRequest(
        classify_target=classify_target,
    )

    # Make the request
    response = client.classify(request=request)

    # Handle the response
    print(f"Mollusc is a \"{response.taxonomy}\"")

# [END mollusc_classify_sync]
