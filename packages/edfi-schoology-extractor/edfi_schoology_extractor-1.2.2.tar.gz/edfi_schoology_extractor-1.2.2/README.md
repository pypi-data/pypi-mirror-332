# Schoology Extractor

This tool retrieves and writes out to CSV students, active sections†,
assignments, and submissions by querying the Schoology API († sections that are
in an active grading period). For more information on the this tool and its
output files, please see the main repository
[readme](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit).

## Special Notes About Working With Schoology

**Assignments**: the Schoology API appears to have a bug, not returning an assignment's
full text description. The field is in the data model, but will never be populated by
the Schoology Extractor unless and until Schoology fixes the bug.

**Attendance Events**: the Schoology API handles _negative
attendance_ events: if a student is marked as present, or is not marked at all,
then the system will not return a record for that day.

**System activities**: System usage data in Schoology are only available by downloading
a file through the Schoology website. If you wish to track system student use of the
system, then please read [Schoology's instructions on usage
analytics](https://support.schoology.com/hc/en-us/articles/360036884914-Usage-Analytics-New-School-Analytics-Enterprise-).
Each downloaded file needs to be stored in an input directory, and that
directory must be provided to the extractor configuration.

## Getting Started

1. Download the latest code from [the project homepage](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit)
   by clicking on the green "CODE" button and choosing an appropriate option. If choosing
   the Zip option, extract the file contents using your favorite zip tool.
1. Open a command prompt* and change to this file's directory (* e.g. cmd.exe, PowerShell, bash).
1. Ensure you have [Python 3.9+ and Poetry](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit#getting-started).
1. At a command prompt, install all required dependencies:

   ```bash
   poetry install
   ```

1. Optional: make a copy of the `.env.example` file, named simply `.env`, and
   customize the settings as described in the Configuration section below.
1. Open [https://app.schoology.com/api](https://app.schoology.com/api) and
   sign-in with an administrative account to acquire an API key and secret; if
   using a `.env` file, insert those values into the file.
1. Run the extractor one of two ways:
   * Execute the extractor with minimum command line arguments:

      ```bash
      poetry run python edfi_schoology_extractor -k [schoology client key]
          -s [schoology client secret] -f assignments
      ```

   * Alternately, run with environment variables or `.env` file:

     ```bash
     poetry run python edfi_schoology_extractor
     ```

   * For detailed help, execute `poetry run python canvas_extractor -h`.

## Configuration

Application configuration is provided through environment variables or command
line interface (CLI) arguments. CLI arguments take precedence over environment
variables. Environment variables can be set the normal way, or by using a
dedicated [`.env` file](https://pypi.org/project/python-dotenv/). For `.env`
support, we provided a [.env.example](.env.example) which you can copy, rename
to `.env`, and adjust to your desired parameters. Supported parameters:

| Description | Required | Command Line Argument | Environment Variable |
| ----------- | -------- | --------------------- | -------------------- |
| Schoology API Key | yes | `-k` or `--client-key` | SCHOOLOGY_KEY |
| Schoology API Secret | yes | `-s` or `--client-secret` | SCHOOLOGY_SECRET |
| Usage analytics input directory | no | `-i` or `--input-directory` | SCHOOLOGY_INPUT_DIRECTORY |
| Output Directory | no (default: [working directory]/data) | `-o` or `--output-directory` | OUTPUT_DIRECTORY |
| Sync database directory | no (default: [working directory]/data) | `-d` or `--sync-database-directory` | SYNC_DATABASE_DIRECTORY |
| Log level** | no (default: INFO) | `-l` or `--log-level` | LOG_LEVEL |
| Page size | no (default: 20) | `-p` or `--page-size` | PAGE_SIZE |
| Number of retry attempts for failed API calls | no (default: 4) | none | REQUEST_RETRY_COUNT |
| Timeout window for retry attempts, in seconds | no (default: 60 seconds) | none | REQUEST_RETRY_TIMEOUT_SECONDS |
| Feature*** | no (default: core, not removable) | `-f` or `--feature` | FEATURE |

\** Valid values for the optional _log level_:

* DEBUG
* INFO(default)
* WARNING
* ERROR
* CRITICAL

\*** When there's no specified feature, the extractor will always process Users,
Sections, and Section Associations, which are considered the core feature. Other
features (can combine two or more):

* assignments (Enables the extraction of assignments and submissions)
* attendance (Enables the extraction of attendance events)
* activities (Enables the extraction of section activities and system
  activities) - **EXPERIMENTAL**, subject to breaking changes
* grades (Enables the extraction of grades) - **COMING SOON**

When setting features via `.env` file or through environment variable, combine
features by using a bracketed comma-separate list, e.g. `FEATURE=[activities,
attendance, assignments, grades]`. To combine features at the command line,
simply list them together: `--feature activities, attendance, assignments,
grades`.

### Logging and Exit Codes

Log statements are written to the standard output. If you wish to capture log
details, then be sure to redirect the output to a file. For example:

```bash
poetry run python edfi_schoology_extractor > 2020-12-07-15-43.log
```

If any errors occurred during the script run, then there will be a final print
message to the standard error handler as an additional mechanism for calling
attention to the error: `"A fatal error occurred, please review the log output
for more information."`

The application will exit with status code `1` if there were any log messages at
the ERROR or CRITICAL level, otherwise it will exit with status code `0`.

## Developer Operations

1. Style check: `poetry run flake8`
1. Static typing check: `poetry run mypy .`
1. Run unit tests: `poetry run pytest`
1. Run unit tests with code coverage: `poetry run coverage run -m pytest`
1. View code coverage: `poetry run coverage report`

_Also see
[build.py](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/docs/build.md)_ for
use of the build script.

### Visual Studio Code (Optional)

To work in Visual Studio Code install the Python Extension.
Then type `Ctrl-Shift-P`, then choose `Python:Select Interpreter`,
then choose the environment that includes `.venv` in the name.

## Legal Information

Copyright (c) 2022 Ed-Fi Alliance, LLC and contributors.

Licensed under the [Apache License, Version 2.0](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/LICENSE) (the "License").

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.

See [NOTICES](https://github.com/Ed-Fi-Exchange-OSS/LMS-Toolkit/blob/main/NOTICES.md) for
additional copyright and license notifications.
