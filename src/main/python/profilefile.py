import os
from collections import OrderedDict
#import settings_map

class ProfileFile:
    def __init__(self, filename):
        self._filename = filename
        self._profiles = OrderedDict()

    def load(self):
        self._profiles = OrderedDict()
        with open(self._filename, encoding="utf8") as f:           
            profileName = os.path.basename(self._filename)
            for line in f:
                line = line.strip()
                if line.startswith("[") and line.endswith("]"):
                    profileName = line[1:-1]
                elif "=" in line:
                    try:
                        (key, value) = line.split("=")
                        if key.startswith(";"):
                            key = key[1:]
                        key = key.strip().replace(" ", "_")
                        if profileName not in self._profiles:
                            self._profiles[profileName] = {}
                        self._profiles[profileName][key] = value.strip()
                    except ValueError:
                        pass 

    def fileName(self):
        return self._filename
               
    def profiles(self):
        return self._profiles.keys()

    def keys(self, profile):
        return self._profiles[profile].keys()

    def value(self, profile, key):
        if key in self._profiles[profile]:
            return self._profiles[profile][key]
        return ""

class ProfileCollection:
    def __init__(self):
        self._files = []
        self._data = []
        self._keys = []
        self._profiles = []
        self._filterIdentical = False
        self._filterSingle = False

    def _rebuild(self):
        self._keys = []
        self._data = []
        self._profiles = []
        all_keys = {}

        for file in self._files:
            for profile in file.profiles():
                self._profiles.append(profile)
                self._data.append([])
                for key in file.keys(profile):
                    all_keys[key] = 1

        for key in all_keys.keys():
            row = []
            for file in self._files:
                for profile in file.profiles():
                    row.append(file.value(profile, key))
            # Check if filtering applies
            if len(row) == 1:
                self._data[0].append(row[0])
                self._keys.append(key)
            else:
                single_value = True
                identical_values = True
                for i in range(len(row)-1):
                    if row[i] != row[i+1]:
                        identical_values = False
                if row.count("") < len(row) - 1:
                    single_value = False
                if not (self._filterIdentical and identical_values or self._filterSingle and single_value):
                    for i in range(len(row)):
                        self._data[i].append(row[i])
                    self._keys.append(key)

    def addFile(self, filename):
        if not self.refreshFile(filename):
            file = ProfileFile(filename)
            file.load()
            self._files.append(file)
            self._rebuild()

    def refreshFile(self, filename):
        for f in self._files:
            if f.fileName() == filename:
                f.load()
                self._rebuild()
                return True
        return False

    def removeFile(self, filename):
        for f in self._files:
            if f.fileName() == filename:
                self._files.remove(f)
                self._rebuild()

    def profileName(self, profileNum):
        return self._profiles[profileNum]

    def data(self, profile, index):
        return self._data[profile][index]

    def profileCount(self):
        return len(self._profiles)

    def parameterCount(self):
        return len(self._keys)

    def parameterName(self, index):
        return self._keys[index]

    def setFilters(self, filterIdentical, filterSingle):
        self._filterIdentical = filterIdentical
        self._filterSingle = filterSingle
        self._rebuild()

