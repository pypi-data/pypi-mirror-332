# Beancount Triodos Importer

beancount-triodos-importer provides a python import script for beancount to
import CSV exports from triodos online banking.

## Usage

### Installation

Install `beancounttriodos` from pip like this:

```bash
    pip install beancounttriodos
```


### Configuration

Write a configuration file, eg. `config.py`, (or extend your existing one) to include this:

```python
    import beangulp
    import beancounttriodos

    CONFIG = [
        beancounttriodos.CSVImporter('NL12TRIO3456789012', 'Assets:Your:Account')
    ]

    if __name__ == '__main__':
        main = beangulp.Ingest(CONFIG)
        main()
```

Your IBAN account number (`NL12TRIO3456789012` in the example) will be
used by `beangulp` to match with the CSV export from the website.


### Daily use

 1. Download the CSV file from your triodos online banking,
 2. Run `config.py extract transaction_file.csv`


## License

This package is licensed under the MIT License.

