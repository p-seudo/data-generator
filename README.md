
# Data Generator

Data Generator, simulates data for a hypothetical retail analytics company. The story is that this retail analytics company receives monthly sales data from various distributors from accross the country. Why? So that you can learn data warehousing/engineering/analysis and BI report building using any of the tools out there from an actual use case.

##### Manufacturing Enterprises Associated with the hypothetical retail analytics company
There are a total of 10 Manufacturers associated with this company (ofcourse hypothetically). I really hope none of them sue me for mentioning their names. In my defence I keep saying "Hypothetical"
| Manufacturer Code | Manufacturer Name |
| ------ | ------ |
| 601 | Hindustan Unilever Ltd. |
|602 | Procter & Gamble Hygiene and Health Care Ltd.|
| 603| Nestle India Ltd.|
|604 | Dabur India Ltd. | 
| 605 | Patanjali Ayurved Ltd. |
|606 | Britannia Industries Ltd. |
| 607 | Colgate-Palmolive (India) Ltd. |
| 608 | ITC Ltd. |
| 609 | Marico Ltd. |
| 610 | Godrej Consumer Products Ltd.

The narration is that, the retail analytics company receives master data of the items that they work with and all the distributors as `master files` as present inside the `master/` directory. 
1. master_manufacturer.csv - contains manufacturer codes along with manufacturer names
2. master_item.csv - contains all the items from all the enterprises along with their manufacaturer mappings (manufacturer_code)
3. master_dc.csv - contains distributor/distribution center information. 

Note that the narration dictates all distributors work with all manufacturers. 

What do you do?
1. Load the master files into your Data Warehouse (come up with your own design)
2. Run the generator to build data files (one for each distributor) for a specified month
3. Build an ETL/ELT pipeline to load, transform to whatever granularity you want your Data Marts to work with
4. Build BI reports (if you want to)

How do you do this? 
*Having python in your local machine is a given.*
1. First clone the repository
2. cd into the folder and install all the dependencies using pip
    ```sh
    pip3 install -r requirements.txt
    ```
3. Run the generator with a period argument (a period as in a month-year).
    ```sh
    python3 generate.py -p 02-2024
    ```
4. You get one file for each distributor inside the `sales_file/<dc-code>` directory in MMYYY.csv format
5. Well, from there on push data into your pipeline and build your data marts.
