import torch
from torch_geometric.data import Data
from newtonnet.utils.ase_interface import MLAseCalculator
from newtonnet.data.neighbors import RadiusGraph

from .base_potential import BasePotential, PotentialOutput

class NewtonNetPotential(BasePotential):
    def __init__(self, model_path, **kwargs):
        """
        Constructor for NewtonNetPotential

        Parameters
        ----------
        model_path: str or list of str
            path to the model. eg. '5k/models/best_model_state.tar'
        settings_path: str or list of str
            path to the .yml setting path. eg. '5k/run_scripts/config_h2.yml'
        device: 
            device to run model. eg. 'cpu', ['cuda:0', 'cuda:1']
        kwargs
        """
        super().__init__(**kwargs)
        self.model = self.load_model(model_path)
        self.transform = RadiusGraph(self.model.embedding_layer.norm.r)
        self.n_eval = 0

    
    def forward(self, points):
        data = self.data_formatter(points)
        pred = self.model(data.z, data.disp, data.edge_index, data.batch)
        self.n_eval += 1
        energy = pred.energy
        force = pred.gradient_force
        energy = energy.view(-1, 1)
        force = force.view(*points.shape)
        return PotentialOutput(energy=energy, force=force)
        

    def load_model(self, model_path):
        calc = MLAseCalculator(model_path, properties=['energy', 'forces'], device=self.device)
        model = calc.models[0]
        model.eval()
        model.output_layers[1].create_graph = True
        model.to(torch.float64)
        model.requires_grad_(False)
        model.embedding_layer.requires_dr = False
        return model
    
    def data_formatter(self, pos):
        n_atoms = self.n_atoms
        n_data = pos.numel() // (n_atoms * 3)
        z = self.numbers.repeat(n_data)
        pos = pos.view(n_data * n_atoms, 3)
        lattice = torch.ones(1, device=self.device) * torch.inf
        batch = torch.arange(n_data, device=self.device).repeat_interleave(n_atoms)
        data = Data(pos=pos, z=z, lattice=lattice, batch=batch)
        
        return self.transform(data)
