# DoData python library 0.7.0

In chip design, managing a variety of data types is essential:

- Simulations
- Layouts
- Verification results (DRC, LVS ...)
- Measurements
- Yield, qualification data

![data-wave](https://i.imgur.com/A6l1g3D.png)

DoData delivers a cutting-edge data storage solution specifically crafted for the complexities of chip design. Our platform seamlessly integrates into your existing workflow, offering a scalable approach to store, manage, and analyze all your critical data files, enhancing both efficiency and effectiveness in your design process.

![data-types](https://i.imgur.com/DVDGNFm.png)

![device-die-wafer](https://i.imgur.com/v8wlnFr.png)

## Installation

We only support Python 3.11 or 3.12, and recommend [VSCode](https://code.visualstudio.com/) IDE and UV. You can install UV on a terminal with the following commands:

```bash
# On macOS and Linux.
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
# On Windows.
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Then you can install dodata with:

```
uv pip install "dodata[demos]" --upgrade
```

## Setup

Ensure you create a .env file in your working directory with the following contents:

```
dodata_url = 'https://your.dodata.url.here'
dodata_user = 'dodata_user'
dodata_password = 'dodata_web_password'
dodata_db = 'your.dodata.database.url.here'
dodata_db_user = "db_username_here"
dodata_db_password = "db_password_here"
dodata_db_name = "dodata"
data_db_port = 5432
debug = False
```

The .env file should be in the same directory where you run the notebooks or in a parent directory.

## Run notebooks

To run the notebooks, you can use either VSCode or JupyterLab:

- VSCode: Ensure you select the same Conda Python interpreter where the packages were installed.
- JupyterLab: Launch JupyterLab by running jupyter-lab from the same terminal used for the installation.

Run the notebooks in the following order:

- `1_generate_layout`: Generates the GDS layout and a CSV device manifest, including device coordinates, settings, and analysis.
- `2_generate_measurement_data`: Generates CSV measurement data.
- `3_upload_measurements`: Uploads wafer definitions, measurement data and trigger analysis.
- `4_download_data`: Downloads analysis using specific queries.
- `5_delete`: Deletes data as needed.
