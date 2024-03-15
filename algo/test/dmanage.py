import statistics
import math

class Dmanage:

    url = None
    dataset = None

    def __init__(self):
        pass


    def __init__(self, cols=None, data=None):

        self.dataset = {}
        self.dataset["cols"] = cols
        self.dataset["data"] = data
        


    def get_csv(self, url):

        self.url = url

        with open(url, "r") as file:

            x = file.readline().strip()
            cols = x.split(",")
            
            x = file.readline().strip()

            data = []

            while x:
                temp_dict = {}
                col_data = x.split(",")
                for k, col in enumerate(cols):

                    
                    temp_dict[col] = float(col_data[k]) if col_data[k].isnumeric() else True if col_data[k].lower() == "true"  else False if col_data[k].lower() == "false" else col_data[k] 

                data.append(temp_dict)
                
                x = file.readline().strip()
            
        self.dataset = {"cols": cols, "data": data}

        return Dmanage(cols=self.dataset.copy()["cols"], data=self.dataset.copy()["data"])

    def show_csv(self):

        cols = self.dataset["cols"]
        datapart = self.dataset["data"]

        print("C\t" + "\t".join(cols))
        for k , col_data in enumerate(datapart):
            print(f"{k}\t" + "\t".join( [str(col_data[xx]) for xx in cols] ))

    def mean(self, col_name):

        datapart = self.dataset["data"]

        one_col_data = [col_data[col_name] for col_data in datapart ]

        return statistics.mean(one_col_data)
    

    def length(self):

        return len(self.dataset["data"])
    

    def stdv(self, col_name):

        datapart = self.dataset["data"]

        one_col_data = [col_data[col_name] for col_data in datapart ]

        mean_value = statistics.mean(one_col_data)

        sum = 0

        for col_value in one_col_data:
            sum += (col_value - mean_value)**2

        return math.sqrt( sum/len(self.dataset["data"]) )
    

    def filter(self, items):

        data = self.dataset["data"]
        filtered_data = [{it: d[it] for it in items} for d in data]
        # self.dataset["cols"] = items
        # self.dataset["data"] = filtered_data
        return Dmanage(cols=items, data=filtered_data)
    
    def filterby_colval(self, col, val):

        data = self.dataset["data"]
        filtered_data = []

        for data in self.dataset["data"]:
            
            if data[col] == val:
                filtered_data.append(data)
                    
                
        # self.dataset["cols"] = items
        # self.dataset["data"] = filtered_data
        # return Dmanage(cols=items, data=filtered_data)
        return Dmanage(data=filtered_data, cols=self.dataset.copy()["cols"])
    
    def unique(self, col):

        uniques = []

        for data in self.dataset["data"]:
            if not data[col] in uniques:
                uniques.append(data[col])

        return uniques
    
    def aggregate(self, group_by, col):

        unique_list = self.unique(col)

        

        agg = {}

       

        for unique in unique_list:
            filtered_data = []
            agg[unique] ={}
            for data in self.dataset["data"]:

                if(data[col] == unique):
                    temp_dict = {group_by: data[group_by]}
                    temp_dict[col] = data[col]
                    filtered_data.append(temp_dict)
            
            tmp_group_by_item = [ fil[group_by] for fil in filtered_data ]

            

            agg[unique]["count"] = len(filtered_data)

            mean_value = statistics.mean(tmp_group_by_item)

            sum = 0

            for group_by_item in tmp_group_by_item:
                sum += (group_by_item - mean_value)**2

            agg[unique]["std"] = math.sqrt( sum/len(tmp_group_by_item) )

            
        return agg
    

    def copy(self):
        return Dmanage(data=self.dataset.copy()["data"], cols=self.dataset.copy()["cols"])

                

        
            
            

        # return agg

        


# dm = Dmanage()
# dm = dm.get_csv("./fake_ds.csv")

# dm.show_csv()

# print(dm.stdv("HoursPlayed"))

# print(dm.filter(items=["Temp", "Windy", "HoursPlayed"]).show_csv())
