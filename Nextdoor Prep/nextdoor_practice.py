cities = [
  {
    "name": "Bay Area",
    "id": 1,
    "parent_id": 99
  },
  {
    "name": "California",
    "id": 99,
    "parent_id": null
  },
  {
    "name": "Oakland",
    "id": 2,
    "parent_id": 1
  },

{
    "name": "Nextdoor NOPA",
    "id": 3,
    "parent_id": 6
  },
  {
    "name": "San Francisco",
    "id": 6,
    "parent_id": 8
  },
  {    
     "name": "San Francisco County",     
     "id": 8,     
      "parent_id": 1   
    },
{     
	"name": "New York City",     
	"id": 4,     
	"parent_id": None  
 },   
{     
	"name": "Brooklyn",     
	"id": 9,    
	 "parent_id": 4   
},   
{     
	"name": "Queens",
	"id": 5,     
	"parent_id": 4   
},
]

def print_cities_by_level(cities):
    # Go through the list of cities and store them in a map so we can easily access them
    # As I go through the list, I will also connect the children cities to the parents

    