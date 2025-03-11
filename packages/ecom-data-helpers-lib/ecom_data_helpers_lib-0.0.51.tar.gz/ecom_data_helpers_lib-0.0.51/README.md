#

##
python setup.py sdist
twine upload --verbose dist/*

pip install ecom_data_helpers_lib==0.0.50