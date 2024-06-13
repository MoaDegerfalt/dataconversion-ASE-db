from ase.db import connect
from ase.io import write

# Function to read data from ASE-db format
def read_data_from_db(db_file):
    atoms_list = []
    with connect(db_file) as db:
        for row in db.select():
            atoms = row.toatoms()
            atoms.info['energy'] = row.data.energy
            atoms.arrays['forces'] = row.data.forces
            atoms.info['stress'] = row.data.stress
            atoms_list.append(atoms)
    return atoms_list


# Main function to convert ASE-db format to ASE extended XYZ format
def convert_to_extxyz(db_file, output_file):
    atoms_list = read_data_from_db(db_file)
    # Writing to extxyz file
    for atoms in atoms_list:
        write(output_file, atoms, format='extxyz', append=True)


if __name__ == "__main__":
    db_file = 'validation.db'
    output_file = 'validation.extxyz'
    convert_to_extxyz(db_file, output_file)

