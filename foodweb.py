import matplotlib.pyplot as plt
import networkx as network


class SaltMarshFoodweb:
    def __init__(self,type,name,description=None,environment=None,contaminant=None):
        self.name = name
        self.type = type
        self.description = description
        self.environment = environment
        self.contaminant = contaminant
        self.species = []


    # Returns the properties of the food web
    def get_properties(self):
        properties = {
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'species': self.species,
            'environment': self.environment
        }
        return properties


    # Adds a node to the list of species in the food web
    def add_species(self,name,specie):
        node = {
            'name': name,
            'specie': specie
        }
        self.species.append(node)
        return self.species


    # Removes a node from the list of species in the food web
    def remove_species(self,name):
        try:
            for node in self.species:
                if node['name'] == name:
                    self.species.remove(node)
            return self.species

        except Exception as error:
            print(error)


    def get_species(self):
        return self.species

    def get_species_names(self):
        names = []
        for specie in self.species:
            names.append(specie['name'])
        return names


    # Returns the length of the food web
    def get_foodweb_length(self):
        return len(self.species)


    def summarize(self):
        properties = self.get_properties()
        foodchain = properties['chain']
        environment = properties['environment']
        if environment is not None:
            environmental_properties = environment.get_properties()
        names = []

        for property in properties:
            if property != 'chain' and property != 'environment':
                print(f"{property}: {properties[property]}")
        if environment is not None:
            print(f"Environmental properties: {environmental_properties}")

        for node in foodchain:
            names.append(node['name'])
        print(f"Speices: {names}")
        print(f"Food web length: {len(names)}")


    def visualize(self):
        species_list = []
        graph = network.DiGraph()

        for specie in self.species:
            graph.add_node(specie['specie'].name)
            for prey in specie['specie'].preys:
                graph.add_edge(prey.name,specie['specie'].name)
            # for prey in specie['prey'].preys:
            #     graph.add_edge(prey.name,specie['specie'].name)

        pos = network.spring_layout(graph)
        plt.figure(figsize=(10,7))
        network.draw(G=graph,pos=pos,with_labels=False,font_size=5,font_weight='bold',
                     node_size=[specie['specie'].biomass for specie in self.species],arrowsize=8)
        # network.draw_networkx_edge_labels(G=graph,pos=pos,edge_labels={(u,v): " " for u,v in graph.edges()},font_color='red')
        for node, (x, y) in pos.items():
            plt.text(x, y, node, fontsize=8, ha='left', va='bottom', bbox=dict(facecolor='lightblue', alpha=0.5, edgecolor='black', boxstyle='round,pad=0.2'))
        plt.title(f"{self.name}")
        plt.show()







