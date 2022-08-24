from oceanbolt.sdk.client import APIClient
import pandas as pd


class FleetManagement:
    r"""FleetManagement provides an interface to manage fleets for clients

    Methods:
        create_fleet(): Creates a new Fleet for the current user.
        list_fleets(): Lists Fleets for the current user (or fleets that are
            shared with the current user)
        describe_fleet(): Retrieves fleet by Fleet id.
        delete_fleet(): Deletes a Fleet for the current user.
        rename_fleet(): Changes the name of a Fleet.
        share_fleet(): Sets the shared status of the Fleet to be shared.
        unshare_fleet(): Sets the shared status of the Fleet to be not shared.
        list_vessels(): Retrieves list of vessels in a Fleet.
        add_vessel(): Adds new vessel to a Fleet. A maximum of 1000 vessels
            can be added to a fleet.
        update_vessel(): Updates existing metadata for a Vessel.
        delete_vessel(): Removes a vessel from a Fleet.
        batch_add_vessels(): Batch adds vessels into a Fleet. A maximum of 1000
            vessels can be added to a fleet.
        batch_add_vessels_from_csv(): Batch adds vessels into a Fleet sourced from a CSV file. A maximum of 1000
            vessels can be added to a fleet.
        drop_vessels(): Drops all the vessels currently in a fleet.
        replace_vessels(): Replaces the existing vessels in a Fleet with a batch
            of new vessels. This is equivalent to first calling
            DropVessels and then calling BatchAddVessels. A maximum
            of 1000 vessels can be added to a fleet.
        replace_vessels_from_csv(): Replaces the existing vessels in a Fleet with a batch
            of new vessels sourced from a CSV file. This is equivalent to first calling
            DropVessels and then calling BatchAddVessels. A maximum
            of 1000 vessels can be added to a fleet.





    """

    def __init__(self, client: APIClient):
        self.client = client._fleet_client()
        self.metadata = client.metadata

    def create_fleet(self, **kwargs):
        return self.client.create_fleet(request=kwargs, metadata=self.metadata)

    def list_fleets(self, **kwargs):
        return self.client.list_fleets(request=kwargs, metadata=self.metadata)

    def describe_fleet(self, **kwargs):
        return self.client.describe_fleet(request=kwargs, metadata=self.metadata)

    def delete_fleet(self, **kwargs):
        return self.client.delete_fleet(request=kwargs, metadata=self.metadata)

    def rename_fleet(self, **kwargs):
        return self.client.rename_fleet(request=kwargs, metadata=self.metadata)

    def share_fleet(self, **kwargs):
        return self.client.share_fleet(request=kwargs, metadata=self.metadata)

    def unshare_fleet(self, **kwargs):
        return self.client.unshare_fleet(request=kwargs, metadata=self.metadata)

    def drop_vessels(self, **kwargs):
        return self.client.drop_vessels(request=kwargs, metadata=self.metadata)

    def batch_add_vessels(self, **kwargs):
        return self.client.batch_add_vessels(request=kwargs, metadata=self.metadata)

    def replace_vessels(self, **kwargs):
        return self.client.replace_vessels(request=kwargs, metadata=self.metadata)

    def add_vessel(self, **kwargs):
        return self.client.add_vessel(request=kwargs, metadata=self.metadata)

    def delete_vessel(self, **kwargs):
        return self.client.delete_vessel(request=kwargs, metadata=self.metadata)

    def update_vessel(self, **kwargs):
        return self.client.update_vessel(request=kwargs, metadata=self.metadata)

    def list_vessels(self, **kwargs):
        return self.client.list_vessels(request=kwargs, metadata=self.metadata)

    def replace_vessels_from_csv(self, fleet_id, path):
        r"""
        Args:
            fleet_id (str): Fleet identifier
            path (str): path to the csv file with vessels
        """
        df = pd.read_csv(path)
        if 'imo' not in df.columns:
            print("column 'imo' is required - not found in csv file")
            raise ValueError
        df = df.astype(str)
        df["imo"] = df["imo"].astype(int)
        df.set_index("imo", inplace=True)
        fleet_dict = df.to_dict("index")
        vessels = []

        for key, value in fleet_dict.items():
            vessels.append({"imo": key, "metadata": value})

        return self.client.replace_vessels(request={"fleet_id": fleet_id, "vessels": vessels}, metadata=self.metadata)

    def batch_add_vessels_from_csv(self, fleet_id, path):
        r"""
        Args:
            fleet_id (str): Fleet identifier
            path (str): path to the csv file with vessels
        """
        df = pd.read_csv(path)
        if 'imo' not in df.columns:
            print("column 'imo' is required - not found in csv file")
            raise ValueError
        df = df.astype(str)
        df["imo"] = df["imo"].astype(int)
        df.set_index("imo", inplace=True)
        fleet_dict = df.to_dict("index")
        vessels = []

        for key, value in fleet_dict.items():
            vessels.append({"imo": key, "metadata": value})

        return self.client.batch_add_vessels(request={"fleet_id": fleet_id, "vessels": vessels}, metadata=self.metadata)
