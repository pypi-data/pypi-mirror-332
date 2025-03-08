
# EIDA Embargo Roller

## Description
This program processes a `stationXML` file in input and updates channels epochs to reflect the embargo start date specified.

1. **If the channel epoch ends before the embargo**: No changes are made.
2. **If the channel epoch ends after the embargo**:
   - If the epoch starts before the embargo and the restriction policy is **closed**, the epoch is split at the embargo date:
     1. The restriction policy before the embargo is forced to **open**.
     2. The restriction policy after the embargo remains **closed**.
3. After processing, the program merges channels that are contiguous in time and have the same content.

---

## Usage

```bash
eida_embargo_roller [-i] [-e YYYY-MM-DD] station.xml
```
### Options:
- `-i`: Transform the `stationXML` file provided in place.
- `-e`: Embargo start date. All channels before this date will get unrestricted policy.

---

## Examples

### Writing a New XML File
Writing a new XML file for an embargo date:
```bash
uv run eida_embargo_roller Z3.A190A.xml -e 2023-01-01 > result.xml
```

### Changing an existing XML file:
Transform the file in place:
```bash
uv run eida_embargo_roller -e 2025-01-01 -i Z3.A190A.xml
```


## Installation

### Using UV (Recommended)

### 1. Install uv

If uv is not already installed, you can add it by following [this guide](https://docs.astral.sh/uv/getting-started/installation/).


### 2. Sync Dependencies
Navigate to the project directory and run:
```bash
uv sync 
```
This command will install all dependencies listed in `pyproject.toml`.

### 3. Run the Script
After syncing, use:
```bash
uv run eida_embargo_roller -e YYYY-MM-DD station.xml
```
#### **Rust and Cargo Requirement**

Certain dependencies (e.g., `pendulum`) require Rust and Cargo to build. If you encounter errors such as `maturin` failing due to missing Cargo, install Rust and Cargo by following the [official Rust installation guide](https://doc.rust-lang.org/cargo/getting-started/installation.html).
### As a Python Package
To install using pip:
```bash
python -m pip install --user eida_embargo_roller
```

### From Source
To install from source:
```bash
git clone https://github.com/your-repo/embargo-roller.git
cd embargo-roller

# Install dependencies using UV
uv sync

```
## **Tests and Debugging**

### Running Tests
To run the entire test suite using `pytest`, execute:
```bash
uv run pytest
```

# PyPI package

 The EIDA Embargo Roller is also available as a PyPI package: https://pypi.org/project/eida-embargo-roller/


# Updating SeisComP configuration 
Embargo roller works with FDSN XML only, not with inventoryXML used by SeisComP. Following steps describe the procedure for updating config:
1. Convert to stationXML:
```bash
   fdsnxml2inv --to-staxml inventory.xml > FDSNstation.xml
```
2. Update embargo period:
```bash
   uv run eida_embargo_roller -e 2022-12-31 FDSNstation.xml > FDSNstation-embargoFree.xml
```
3. Replace restrictedStatus “partial” by “open” in FDSNstation-embargoFree.xml (Seiscomp does not recognize “partial” status):
```bash
   sed -e 's/"partial"/"open"/'
```
4. Convert FDSNstation-embargoFree.xml to invXML:
```bash
   fdsnxml2inv FDSNstation-embargoFree.xml > inventory-embargoFree.xml
```
5. Update SEISCOMP:
```bash
   scinv sync [--test]
   seiscomp update-config
   seiscomp restart
```
6. Test query for open data:
https://EIDA-node/fdsnws/dataselect/1/query?start=2022-12-22T00:00:00&end=2022-12-22T00:10:00&net=XX&sta=YYY&cha=*Z
