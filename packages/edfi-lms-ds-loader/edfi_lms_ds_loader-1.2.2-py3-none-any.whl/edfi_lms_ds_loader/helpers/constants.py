# SPDX-License-Identifier: Apache-2.0
# Licensed to the Ed-Fi Alliance under one or more agreements.
# The Ed-Fi Alliance licenses this file to you under the Apache License, Version 2.0.
# See the LICENSE and NOTICES files in the project root for more information.

LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]


class DbEngine:
    MSSQL = "mssql"
    POSTGRESQL = "postgresql"


class Table:
    # Table names are all lower case for PostgreSQL compatibility
    USER = "lmsuser"
    SECTION = "lmssection"
    ASSIGNMENT = "assignment"
    ASSIGNMENT_SUBMISSION_TYPES = "assignmentsubmissiontype"
    ASSIGNMENT_SUBMISSION = "assignmentsubmission"
    SECTION_ASSOCIATION = "lmsuserlmssectionassociation"
    SECTION_ACTIVITY = "lmssectionactivity"
    SYSTEM_ACTIVITY = "lmssystemactivity"
    ATTENDANCE = "lmsuserattendanceevent"
