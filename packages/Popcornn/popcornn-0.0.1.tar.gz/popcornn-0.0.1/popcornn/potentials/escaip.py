import torch
from torch import nn
from torch_geometric.data import Data
import yaml
from ase import units
import os
import numpy as np
from fairchem.core.common.relaxation.ase_utils import OCPCalculator
from torch_geometric.data import Data

import sys
sys.path.append('/global/homes/e/ericyuan/GitHub/EScAIP')

from .base_potential import BasePotential, PotentialOutput

class EScAIPPotential(BasePotential):
    def __init__(self, config_yml, checkpoint_path, cpu, **kwargs):
        super().__init__(**kwargs)
        calc = OCPCalculator(config_yml=config_yml, checkpoint_path=checkpoint_path, cpu=cpu)
        self.trainer = calc.trainer
        self.trainer.model.eval()    
        if self.trainer.ema is not None:
            self.trainer.ema.store()
            self.trainer.ema.copy_to()
        self.trainer.model.requires_grad_(False)

    def forward(self, points):
        data = self.data_formatter(points)
        pred = self.trainer.model(data)
        for key in pred.keys():
            pred[key] = self.trainer._denorm_preds(key, pred[key], data)
        energy = pred['energy'].view(-1)
        force = pred['forces'].view(*points.shape)
        return PotentialOutput(energy=energy, force=force)

    def data_formatter(self, pos):
        pos: torch.Tensor = pos.float()
        numbers: torch.Tensor = self.numbers
        cell: torch.Tensor = self.cell.float()
        pbc: torch.Tensor = self.pbc
        tags: torch.Tensor = self.tags
        n_atoms: int = self.n_atoms
        n_data: int = pos.shape[0]
        
        data = Data(
            atomic_numbers=numbers.repeat(n_data), 
            pos=pos.view(n_data * n_atoms, 3), 
            cell=cell.repeat(n_data, 1, 1),
            batch=torch.arange(n_data, device=self.device).repeat_interleave(n_atoms),
            natoms=torch.tensor(n_atoms, device=self.device).repeat(n_data), 
            num_graphs=n_data, 
            tags=tags.repeat(n_data),
        )

        return data
