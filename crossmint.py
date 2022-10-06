# Mateo Fernandez Lopez Areal - Oct 5
# IMPORTS
import requests
import json
import numpy as np

class Map:
    """
    Phase 1 & Phase 2 Crossmint Class

    """
    def __init__(self, candidateID):
        """
        Constructor for Map class

        :param candidateID: str; Idnetification for each candidate in the CROSSMINT coding challenge
        """
        self.candidateID = candidateID
        self.headers =  {"Content-Type":"application/json"}
        # Obtain the goal map asked by the challenge
        self.map = self._getGoalMap()
    
    def _getGoalMap(self):
        """
        Using the Megaverse API, returns the goal map for the current challenge phase

        :return: map: numpy.ndarray; Contains the goal map
        """
        api_url_goal = "".join(["https://challenge.crossmint.io/api/map/",self.candidateID,"/goal"])
        response_goal = requests.get(api_url_goal)
        map = np.array(response_goal.json()['goal'])
        return map
    
    def writePolyanet(self, row, column):
        """
        Using the Megaverse API, writes a Polyanet in the given position

        :param row: int; Position in the row axis
        :param column: int; Position in the column axis
        :param column: int; Position in the column axis
        """
        api_url = "https://challenge.crossmint.io/api/polyanets"
        args = {'candidateId': self.candidateID,'row':row,'column':column}
        requests.post(api_url,data=json.dumps(args), headers=self.headers)

    def writeCometh(self, row, column, direction):
        """
        Using the Megaverse API, writes a Cometh in the given position and direction

        :param row: int; Position in the row axis
        :param column: int; Position in the column axis
        :param direction: str; Direction the Cometh will be facing
        """
        api_url = "https://challenge.crossmint.io/api/comeths"
        args = {'candidateId': self.candidateID,'row':row,'column':column, 'direction':direction}
        requests.post(api_url,data=json.dumps(args), headers=self.headers)

    def writeSoloon(self, row, column, color):
        """
        Using the Megaverse API, writes a Soloon in the given position and color

        :param row: int; Position in the row axis
        :param column: int; Position in the column axis
        :param color: str; Color of the Soloon
        """
        api_url = "https://challenge.crossmint.io/api/soloons"
        args = {'candidateId': self.candidateID,'row':row,'column':column, 'color':color}
        requests.post(api_url,data=json.dumps(args), headers=self.headers)

    def createCopyofGoalMap(self):
        """
        Copies the structure and interior of the goal map

        """
        row_count=0
        for row in self.map:
            column_count=0
            for item in row:
                # Check if item is a POLYANET
                if(item=="POLYANET"):
                    # Write a POLYANET
                    self.writePolyanet(row_count, column_count)
                # If not SPACE, COMETH or SOLOON
                elif(item!='SPACE'):
                    # Both cases use "_" as a separator to define the color or direction
                    item = item.split("_")
                    # Check if item is a COMETH
                    if(item[1] == "COMETH"):
                        # Write a COMETH
                        self.writeCometh(row_count, column_count,item[0].lower())
                    # Check if item is a SOLOON
                    elif(item[1] == "SOLOON"):
                        # Write a SOLOON
                        self.writeSoloon(row_count, column_count,item[0].lower())
                column_count+=1
            row_count+=1

    def createCopyofGoalMap_v2(self):
        """
        Copies the structure and interior of the goal map using a similar method

        """
        row_count=0
        for row in self.map:
            pos_polyanet = [i for i in range(len(row)) if row[i] == "POLYANET"]
            [self.writePolyanet(row_count,column) for column in pos_polyanet]
            pos_cometh = [i for i in range(len(row)) if row[i].endswith("COMETH")]
            [self.writeCometh(row_count,column,row[column].split("_")[0].lower()) for column in pos_cometh]
            pos_soloon = [i for i in range(len(row)) if row[i].endswith("SOLOON")]
            [self.writeSoloon(row_count,column,row[column].split("_")[0].lower()) for column in pos_soloon]
            row_count+=1

cross = Map(candidateID= "060a7b53-62d7-46a4-b7b6-4603254d725e")
cross.createCopyofGoalMap()

"""
class Cross:
    # Phase 1 Crossmint Class
    def __init__(self, length, candidateID):
        
        #Constructor for Map class

        #:param length: int; Length the cross will have starting from the middle of the map (needs the shape of the map to be squared and odd)
        #:param candidateID: str; Idnetification for each candidate in the CROSSMINT coding challenge

        self.length = length
        self.candidateID = candidateID
        self.headers =  {"Content-Type":"application/json"}
        self.rows, self.columns  = self._getShapeMap()

    def _getShapeMap(self):

        #Using the Megaverse API, returns the goal map for the current challenge phase

        #:return: map: numpy.ndarray; Contains the shape of the map
        api_url_goal = "".join(["https://challenge.crossmint.io/api/map/",self.candidateID,"/goal"])
        response_goal = requests.get(api_url_goal)
        return np.array(response_goal.json()['goal']).shape

    def writePolyanet(self, row, column):
        
        #Using the Megaverse API, writes a Polyanet in the given position

        #:param row: int; Position in the row axis
        #:param column: int; Position in the column axis
        
        api_url = "https://challenge.crossmint.io/api/polyanets"
        args = {'candidateId': self.candidateID,'row':row,'column':column}
        requests.post(api_url,data=json.dumps(args), headers=self.headers)

    def createXinMap(self):
        
        #Writes a Cross of Polyanet in the map 

        start_row = int((self.rows- self.length)/2)
        end_row = int((self.rows- self.length)/2 + self.length)
        start_column= int((self.columns- self.length)/2)
        end_column = int((self.columns- self.length)/2 + self.length)
        for (x,y) in zip(range(start_row,end_row),range(start_column,end_column)):
            self.writePolyanet(x, y)
            self.writePolyanet(x, self.columns-y-1)

cross = Cross(length = 7, candidateID= "060a7b53-62d7-46a4-b7b6-4603254d725e")
cross.createXinMap()
"""