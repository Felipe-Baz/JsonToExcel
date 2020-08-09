## JsonToExcel

In this code I made an algorithm to convert the data generated by my research (json) into an excel table.
### Library:

- json
- pandas
- numpy

### Operation

The response data of my research algorithms are generated in a json file with 4 keys, each one being an evaluation method for machine learning algorithms, within these keys I have 7 elements, which correspond to the amount of data used in the testing of my algorithms .

As each code will be executed 30 times I get 30 json files at the end of executions.

So my algorithm turns all these json files into an excel table (initially without formatting), as shown in the image below.

[![figure 1](https://i.imgur.com/TlalYmz.png "figure 1")](https://i.imgur.com/TlalYmz.png "figure 1")

After that this table is easily formatted by hand to have a better view resulting in the table shown in figure 2.

[![figure 2](https://i.imgur.com/Gld2gDY.png "figure 2")](https://i.imgur.com/Gld2gDY.png "figure 2")
