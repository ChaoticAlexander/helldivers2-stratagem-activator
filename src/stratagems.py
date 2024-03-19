import sys
import time
import json
from tkinter import messagebox
from typing import Dict, List
from .modules import Key, Config, log
from .types.stratagems import ActionMap, AvailableActions

class Stratagems:
  bindings: Dict[AvailableActions, int]
  codes: Dict[str, str]
  active_code_sequence: List[str]
  menu_open: bool = False

  def __init__(
    self,
    config: Config,
    action_key: str,
    actions_file_path: str = 'codes.json'
  ):
    self.config = config
    self.map_bindings()
    self.load_key_sequences(actions_file_path)
    self.load_active_key_sequence(action_key)
  
  def map_bindings(self):
    self.bindings = {
      key: self.config[config_key]
      for (key, config_key) in ActionMap.items()
    }
    
  def load_key_sequences(self, file_path):
    try:
      with open(file_path) as f:
        self.codes = json.load(f)
    except FileNotFoundError:
      messagebox.showerror('Error', f'File not found: {file_path}')
      sys.exit(1)
    except json.JSONDecodeError:
      messagebox.showerror('Error', f'Error decoding JSON file: {file_path}')
      sys.exit(1)

  def load_active_key_sequence(self, key):
    if key in self.codes:
      self.active_code_sequence = self.codes[key].split(' ')
    else:
      messagebox.showerror('Stratagem execution error', f'Key "{key}" not found in codes.json')
      sys.exit(1)

  def simulate_key_presses(self):
    for element in self.active_code_sequence:
      Key.press(self.bindings[element])
      time.sleep(0.02)
    
  def toggle_menu(self):
    if (self.config['open_mode'] == 'hold'):
      (Key.down if self.menu_open else Key.up)(self.bindings['O'])
    else:
      Key.press(self.bindings['O'])
      
  def activate(self):
    log(f'Executing stratagem sequence: {self.active_code_sequence}')
    # Open stratagem menu
    self.toggle_menu()
    time.sleep(0.02)

    # Send Key Sequence
    self.simulate_key_presses()

    # Close stratagem menu
    self.toggle_menu()
