from torch.utils.data import Dataset
import pandas as pd
import os

class UserDataset(Dataset):
    def __init__(self, user, item, rating):
        self.user = user
        self.item = item
        self.rating = rating

    def __getitem__(self, index):
        return self.user.iloc[index], self.item.iloc[index], self.rating.iloc[index]
    
    def __len__(self):
        return len(self.user)

    def head(self):
        return self.user.head(), self.item.head(), self.rating.head()

print("UserDataset class defined")


