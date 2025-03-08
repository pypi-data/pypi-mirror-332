import unittest
import tracemalloc
import os
import plotly.graph_objects as go
from glob import glob
import pandas as pd
import matplotlib.pyplot as plt
from Materials_Data_Analytics.metadynamics.free_energy import FreeEnergySpace, MetaTrajectory, FreeEnergyLine, FreeEnergySurface
tracemalloc.start()


class TestMetaTrajectory(unittest.TestCase):
    """
    Test the contruction and behaviour of a meta trajectory
    """
    def setUp(self):
        self.cv_traj = MetaTrajectory("./test_trajectories/ndi_na_binding/COLVAR.0")
        self.opes_traj = MetaTrajectory("./test_trajectories/ndi_single_opes/COLVAR.0")

    def test_colvar_read(self):
        """
        checking that the MetaTrajectory is reading in and processing colvar files correctly. Comparing with a direct
        plumed read in
        """
        self.assertEqual(self.cv_traj._data.columns.to_list(), ['time', 'D1', 'CM1', 'bias', 'reweight_bias', 'reweight_factor', 'weight'])
        self.assertEqual(self.cv_traj.walker, 0)
        self.assertEqual(self.cv_traj.cvs, ['D1', 'CM1'])
        self.assertTrue(self.cv_traj._opes is False)

        self.assertEqual(self.opes_traj._data.columns.to_list(), ['time', 'D1', 'CM1', 'reweight_bias','reweight_factor', 'zed', 'neff', 'nker', 'weight'])
        self.assertEqual(self.opes_traj.walker, 0)
        self.assertEqual(self.opes_traj.cvs, ['D1', 'CM1'])
        self.assertTrue(self.opes_traj._opes is True)


class TestFreeEnergyLineFromPlumedMultiple(unittest.TestCase):

    def setUp(self):
        fes_folder = "./test_trajectories/ndi_na_binding/FES_CM1/"
        self.all_fes_files_list = [file for folder, subdir, files in os.walk(fes_folder) for file in glob(os.path.join(folder, "FES*dat"))]
        self.line = FreeEnergyLine.from_plumed(self.all_fes_files_list)

    def test_fes_read_with_time_data(self):
        """
        checking that alternate constructor works for reading in fes _data with strides to get _time_data dictionary
        """
        individual_files = [f.split("/")[-1] for f in self.all_fes_files_list]
        time_stamps = [int(''.join(x for x in os.path.basename(f) if x.isdigit())) for f in individual_files]
        data_frames = [FreeEnergyLine._read_file(f) for f in self.all_fes_files_list]
        data = {time_stamps[i]: data_frames[i] for i in range(0, len(time_stamps))}
        line = FreeEnergyLine(data)
        compare = pd.read_table("./test_trajectories/ndi_na_binding/FES_CM1/FES2.dat", comment='#', names=['CM1', 'projection'], sep='\s+') 
        energy_diff = compare.loc[1, 'projection'] - compare.loc[2, 'projection']
        my_diff = line._time_data[2].loc[1, 'energy'] - line._time_data[2].loc[2, 'energy']
        self.assertEqual(energy_diff, my_diff)

        compare = pd.read_table("./test_trajectories/ndi_na_binding/FES_CM1/FES2.dat", comment='#', names=['CM1', 'projection'], sep='\s+')
        energy_diff = compare.loc[1, 'projection'] - compare.loc[2, 'projection']
        my_diff = self.line._time_data[2].loc[1, 'energy'] - self.line._time_data[2].loc[2, 'energy']
        self.assertEqual(energy_diff, my_diff)

    def test_normalise_with_float_on_time_data(self):
        """
        testing that the normalise function works with a range
        :return:
        """
        self.line.set_datum(datum={'CM1': 7})
        self.assertTrue(0 in self.line._time_data[0]['energy'])
        self.assertTrue(0 in self.line._time_data[1]['energy'])
        self.assertTrue(0 in self.line._time_data[2]['energy'])
        figure = go.Figure()
        trace = go.Scatter(x=self.line._data[self.line.cvs[0]], y=self.line._data['energy'])
        figure.add_trace(trace)
        # figure.show()

    def test_get_change_over_time(self):
        """
        testing that the normalise function works with a range
        :return:
        """
        change_data = self.line.get_time_difference(1, 3)
        figure = go.Figure()
        trace = go.Scatter(x=change_data['time_stamp'], y=change_data['energy_difference'])
        figure.add_trace(trace)
        # figure.show()

        change_data = self.line.get_time_difference(region_1=(0.8, 1.2), region_2=(2.8, 3.2))
        figure = go.Figure()
        trace = go.Scatter(x=change_data['time_stamp'], y=change_data['energy_difference'])
        figure.add_trace(trace)
        # figure.show()

    def test_set_datum_twice(self):
        """
        testing that the normalise function works with a single value
        :return:
        """
        data1 = self.line.set_datum({'CM1': 3})._data
        data2 = self.line.set_datum({'CM1': 3})._data
        pd.testing.assert_frame_equal(data2, data1)
        figure = go.Figure()
        trace = go.Scatter(x=self.line._data[self.line.cvs[0]], y=self.line._data['energy'])
        figure.add_trace(trace)
        self.assertTrue(0 in self.line._data['energy'])
        # figure.show()

    def test_get_error_from_time_dynamics(self):
        """
        testing that the normalise function works with a range
        :return:
        """
        line = self.line.set_errors_from_time_dynamics(5, bins=100)
        self.assertTrue('energy_err' in line._data.columns.to_list())
        self.assertTrue('population_err' in line._data.columns.to_list())


class TestFreeEnergyLineFromPlumed(unittest.TestCase):

    def setUp(self):
        self.line = FreeEnergyLine.from_plumed("./test_trajectories/ndi_na_binding/FES_CM1.dat")

    def test_attributes(self):
        self.assertEqual(self.line.cvs[0], 'CM1')

    def test_normalise(self):
        """
        testing that the normalise function works with a single value
        :return:
        """
        line = self.line.set_datum({'CM1': 0})
        figure = go.Figure()
        trace = go.Scatter(x=line._data[line.cvs[0]], y=line._data['energy'])
        figure.add_trace(trace)
        self.assertTrue(0 in line._data['energy'])
        # figure.show()

        line = self.line.set_datum(datum={'CM1': (6, 8)})
        self.assertAlmostEqual(line._data.loc[line._data['CM1'] > 6].loc[line._data['CM1'] < 8]['energy'].mean(), 0)
        figure = go.Figure()
        trace = go.Scatter(x=line._data[line.cvs[0]], y=line._data['energy'])
        figure.add_trace(trace)
        # figure.show()


class TestFreeEnergyLine(unittest.TestCase):
    """
    Test the construction and behaviour of a free energy line
    """
    def setUp(self):
        plumed_file = pd.read_table("./test_trajectories/ndi_na_binding/FES_CM1.dat", comment='#', names=['CM1', 'energy'], sep='\s+')
        self.line = FreeEnergyLine(plumed_file)

    def test_attributes(self):
        """
        checking that the 1d fes file is being read in correctly and the cv extracted correctly.
        Comparing with a direct plumed read in
        """
        self.assertEqual(self.line.cvs[0], 'CM1')

    def test_normalise_with_tuple(self):
        """
        testing that the normalise function works with a range
        :return:
        """
        self.line.set_datum(datum={'CM1': (6, 8)})
        self.assertAlmostEqual(self.line._data.loc[self.line._data['CM1'] > 6].loc[self.line._data['CM1'] < 8]['energy'].mean(), 0)
        figure = go.Figure()
        trace = go.Scatter(x=self.line._data[self.line.cvs[0]], y=self.line._data['energy'])
        figure.add_trace(trace)
        # figure.show()


class TestFreeEnergySurface(unittest.TestCase):
    """
    Unittest class to test the FreeEnergySurface class
    """

    def setUp(self):
        self.surface = FreeEnergySurface.from_plumed("./test_trajectories/ndi_na_binding/FES_CM1_D1/FES")

    def test_surface_reader(self):
        """
        Test basic attributes of the surface
        """
        self.assertTrue("energy" in self.surface._data.columns.to_list())
        self.assertTrue("D1" in self.surface._data.columns.to_list())
        self.assertTrue("CM1" in self.surface._data.columns.to_list())
        self.assertTrue("population" in self.surface._data.columns.to_list())

    def test_surface_datum_with_floats(self):
        """
        Test setting the datum with floats
        """
        surface = self.surface.set_datum({'CM1': 0.03, 'D1': 5})
        figure = go.Figure()
        (figure
         .add_trace(go.Contour(
            x=surface._data['CM1'],
            y=surface._data['D1'],
            z=surface._data['energy'],
            colorscale='Jet'))
         )
        self.assertTrue(0 in surface._data['energy'].values.tolist())
        # figure.show()


class TestFreeEnergySpaceFromStandardDirectory(unittest.TestCase):

    def setUp(self):
        self.space = FreeEnergySpace.from_standard_directory("./test_trajectories/ndi_na_binding/", verbose=False, metadata=dict(oligomer='NDI'), temperature=320)

    def test_surface_reweight_with_symmetry(self):
        """
        Test getting a reweighted surface from a FreeEnergySpace object and enforcing symmetry on y=x
        """
        data = (self
                .space
                .get_reweighted_surface(cvs=["CM2", "CM3"], bins=[-0.5, 0.5, 1.5, 2.5, 3.5])
                .set_as_symmetric('y=x')
                .get_data()
                )
        
        figure = go.Figure()
        figure.add_trace(go.Heatmap(x=data["CM2"], y=data["CM3"], z=data['energy']))
        figure.update_layout(template='plotly_dark')
        # figure.show()
        self.assertTrue(type(data) == pd.DataFrame)

        data = (self
                .space
                .get_reweighted_surface(cvs=["CM2", "CM3"], bins=[-0.5, 0.5, 1.5, 2.5, 3.5])
                .set_as_symmetric('y=x')
                .get_data()
                )
        
        figure = go.Figure()
        figure.add_trace(go.Heatmap(x=data["CM2"], y=data["CM3"], z=data['symmetry_error']))
        figure.update_layout(template='plotly_dark')
        # figure.show()
        self.assertTrue(type(data) == pd.DataFrame)

    def test_get_forces(self):
        """
        Test getting the forces of a reweighted surface from a FreeEnergySpace object
        """
        force = (self
                 .space
                 .get_reweighted_surface(cvs=["CM2", "CM3"], bins=[-0.5, 0.5, 1.5, 2.5, 3.5])
                 .set_as_symmetric('y=x')
                 .get_mean_force()
                 .assign(CM2_grad=lambda x: x['CM2_grad']/30)
                 .assign(CM3_grad=lambda x: x['CM3_grad']/30)
                 )

        plt.figure(figsize=(10, 6))
        plt.quiver(force['CM2'], force['CM3'], force['CM2_grad'], force['CM3_grad'], scale=5)
        # plt.show()
        self.assertTrue(type(force) == pd.DataFrame)

    def test_surface_reweighting(self):
        """
        Test getting a reweighted surface from a FreeEnergySpace object
        """
        data = self.space.get_reweighted_surface(cvs=["CM2", "CM3"], bins=[-0.5, 0.5, 1.5, 2.5, 3.5]).get_data()
        figure = go.Figure()
        figure.add_trace(go.Heatmap(x=data["CM2"], y=data["CM3"], z=data['energy']))
        figure.update_layout(template='plotly_dark')
        # figure.show()
        self.assertTrue(type(data) == pd.DataFrame)

    def test_bulk_add_trajectories_alternate_constructors(self):
        """
        testing bulk adding trajectories to a free energy line
        :return:
        """
        self.assertTrue(type(self.space) == FreeEnergySpace)
        self.assertTrue(len(self.space.trajectories) == 2)
        self.assertTrue(self.space.n_walker == 2)
        self.assertTrue(self.space.trajectories[0].temperature == 320)
        self.assertTrue(self.space._metadata['oligomer'] == 'NDI')
        self.assertTrue(self.space.trajectories[0]._metadata['oligomer'] == 'NDI')
        self.assertTrue(self.space.lines['D1'].temperature == 320)
        shape = self.space.get_reweighted_line_with_walker_error('CM1', bins=200)
        self.assertTrue(type(shape) == FreeEnergyLine)
        self.assertTrue(self.space.n_walker == 2)


class TestFreeEnergySpaceFromStandardDirectoryOpes(unittest.TestCase):

    def setUp(self):
        self.landscape = FreeEnergySpace.from_standard_directory("./test_trajectories/ndi_single_opes/", colvar_string_matcher="COLVAR.")


class TestFreeEnergySpaceOpes(unittest.TestCase):

    def setUp(self):
        
        self.landscape = FreeEnergySpace("./test_trajectories/ndi_single_opes/Kernels.data", temperature=320, metadata=dict(oligomer='NDI'))
        self.traj = MetaTrajectory("./test_trajectories/ndi_single_opes/COLVAR.0", temperature=320)
        self.landscape.add_metad_trajectory(self.traj)

    def test_make_landscape(self):
        """
        check that landscape constructor works
        :return:
        """
        self.assertTrue('height' in self.landscape._hills.columns.to_list())
        self.assertTrue('time' in self.landscape._hills.columns.to_list())
        self.assertEqual(type(self.landscape), FreeEnergySpace)
        self.assertEqual(self.landscape.cvs, ['D1', 'CM1'])
        self.assertEqual(self.landscape.n_walker, 1)
        self.assertEqual(self.landscape.n_timesteps, 40)
        self.assertEqual(self.landscape.trajectories[0], self.traj)
        self.assertTrue(type(self.landscape) == FreeEnergySpace)
        self.assertTrue(len(self.landscape.trajectories) == 1)
        self.assertTrue(self.landscape.n_walker == 1)
        self.assertTrue(self.landscape.trajectories[0].temperature == 320)
        self.assertTrue(self.landscape._metadata['oligomer'] == 'NDI')
        self.assertTrue(self.landscape.trajectories[0]._metadata['oligomer'] == 'NDI')

    def test_one_walker_reweighted_with_walker_error(self):
        """
        Function to test that it returns error when only one walker is present.
        :return:
        """
        with self.assertRaises(ValueError):
            self.landscape.get_reweighted_line_with_walker_error("D1", bins=[0, 4, 7]).set_datum({"D1": 0})

    def test_kernels_plotter_default_values(self):
        """
        Test that the kernels plotter works with default values
        """
        figures = self.landscape.get_hills_figures()
        self.assertTrue(self.landscape._opes is True)
        self.assertEqual(len(figures), 1)
        self.assertTrue(figures[0]._validate)
        self.assertEqual(len(figures), 1)
        self.assertTrue(figures[0]._validate)

    def test_two_bin_reweighted_cv_opes(self):
        """
        Function to test that it is normalising properly when using two bins
        :return:
        """
        fes = self.landscape.get_reweighted_line('D1', bins=[0, 0.9, 7]).set_datum({'D1': 0})
        self.assertEqual(fes._data[fes._data['D1'] == 0.45]['energy'].values[0], 0)

        fes = self.landscape.get_reweighted_line('D1', bins=[0, 0.9, 7], conditions='D1 < 5').set_datum({'D1': 0})
        self.assertEqual(fes._data[fes._data['D1'] == 0.45]['energy'].values[0], 0)

        fes = self.landscape.get_reweighted_line('D1', bins=[0, 0.9, 7], n_timestamps=5).set_datum({'D1': 0})
        self.assertEqual(fes._data[fes._data['D1'] == 0.45]['energy'].values[0], 0)
        self.assertTrue(type(fes._time_data) == dict)
        self.assertTrue(type(fes._time_data[1]) == pd.DataFrame)
        self.assertTrue(type(fes._time_data[3]) == pd.DataFrame)
        self.assertTrue(type(fes._time_data[5]) == pd.DataFrame)


class TestFreeEnergySpace(unittest.TestCase):

    def setUp(self):

        self.landscape = FreeEnergySpace("./test_trajectories/ndi_na_binding/HILLS", temperature=320, metadata=dict(oligomer='NDI'))
        self.traj0 = MetaTrajectory("./test_trajectories/ndi_na_binding/COLVAR_REWEIGHT.0", temperature=320)
        self.traj1 = MetaTrajectory("./test_trajectories/ndi_na_binding/COLVAR_REWEIGHT.1", temperature=320)
        self.landscape.add_metad_trajectory(self.traj0)
        self.landscape.add_metad_trajectory(self.traj1)

    def test_make_landscape(self):
        """
        check that landscape constructor works
        :return:
        """
        self.assertTrue('height' in self.landscape._hills.columns.to_list())
        self.assertTrue('time' in self.landscape._hills.columns.to_list())
        self.assertEqual(type(self.landscape), FreeEnergySpace)
        self.assertEqual(self.landscape.cvs, ['D1', 'CM1'])
        self.assertEqual(self.landscape.n_walker, 2)
        self.assertEqual(self.landscape.n_timesteps, 50)
        self.assertEqual(self.landscape.trajectories[0], self.traj0)
        self.assertEqual(self.landscape.trajectories[0].temperature, 320)
        self.assertEqual(self.landscape.trajectories[0]._metadata['oligomer'], 'NDI')

    def test_hills_plotter_default_values(self):
        """
        Test that the hills plotter works with default values
        """
        figures = self.landscape.get_hills_figures()
        self.assertTrue(self.landscape._opes is False)
        self.assertEqual(len(figures), 2)
        self.assertTrue(figures[0]._validate)
        self.assertTrue(figures[1]._validate)

        figure = self.landscape.get_average_hills_figure()
        self.assertTrue(figure._validate)

    def test_fes_adder_checks_work(self):
        """
        Test that the fes adder works
        """
        fes = FreeEnergyLine.from_plumed("./test_trajectories/ndi_na_binding/FES_CM1.dat")
        landscape = self.landscape.add_line(fes)
        self.assertEqual(landscape.lines['CM1'], fes)

    def test_two_bin_reweighted_cv(self):
        """
        Function to test that it is normalising properly when using two bins
        :return:
        """
        fes = self.landscape.get_reweighted_line('D1', bins=[6, 6.5, 7]).set_datum({'D1': 6})
        self.assertEqual(fes._data[fes._data['D1'] == 6.25]['energy'].values[0], 0)

    def test_reweighted_line_cv(self):
        """
        Function to test that it is normalising properly when using two bins
        :return:
        """
        fes = self.landscape.get_reweighted_line('D1', bins=10).set_datum({'D1': 0})
        self.assertEqual(fes._data['energy'].values[0], 0)
        self.assertEqual(round(fes._data['energy'].values[2], 3), 0.827)
        self.assertEqual(round(fes._data['energy'].values[4], 3), 5.648)
        self.assertEqual(round(fes._data['energy'].values[6], 3), 11.103)
        self.assertEqual(round(fes._data['energy'].values[8], 3), 14.089)

        fes = self.landscape.get_reweighted_line('D1', bins=10, adaptive_bins=True).set_datum({'D1': 0})
        self.assertEqual(fes._data['energy'].values[0], 0)
        self.assertEqual(round(fes._data['energy'].values[2], 3), 0.407)
        self.assertEqual(round(fes._data['energy'].values[4], 3), 1.745)
        self.assertEqual(round(fes._data['energy'].values[6], 3), 7.595)
        self.assertEqual(round(fes._data['energy'].values[8], 3), 13.074)

        fes = self.landscape.get_reweighted_line_with_walker_error('D1', bins=10, adaptive_bins=True)
        self.assertEqual(round(fes._data['energy'].values[0], 3), -6.534)
        self.assertEqual(round(fes._data['energy'].values[2], 3), -6.734)
        self.assertEqual(round(fes._data['energy'].values[4], 3), -4.888)
        self.assertEqual(round(fes._data['energy'].values[6], 3), 0.628)
        self.assertEqual(round(fes._data['energy'].values[8], 3), 6.081)

        fes = self.landscape.get_reweighted_line('D1', bins=[6, 6.4, 7], conditions='D1 < 7').set_datum({'D1': 6})
        self.assertEqual(fes._data[fes._data['D1'] == 6.2]['energy'].values[0], 0)

        fes = (self
               .landscape
               .get_reweighted_line('D1', bins=[6, 6.4, 7], conditions=['D1 < 7', 'D1 < 6.8'])
               .set_datum({'D1': 6})
               )
        
        self.assertEqual(fes._data[fes._data['D1'] == 6.2]['energy'].values[0], 0)

        fes = self.landscape.get_reweighted_line('D1', bins=[6, 6.4, 7], n_timestamps=5).set_datum({'D1': 6})
        self.assertEqual(fes._data[fes._data['D1'] == 6.2]['energy'].values[0], 0)
        self.assertTrue(type(fes._time_data) == dict)
        self.assertTrue(type(fes._time_data[1]) == pd.DataFrame)
        self.assertTrue(type(fes._time_data[3]) == pd.DataFrame)
        self.assertTrue(type(fes._time_data[5]) == pd.DataFrame)

        fes = self.landscape.get_reweighted_line_with_walker_error("D1", bins=[6, 6.4, 7], conditions="D1 < 7").set_datum({"D1": 0})
        self.assertEqual(fes._data[fes._data["D1"] == 6.2]["energy"].values[0], 0)
    
        fes = self.landscape.get_reweighted_line_with_walker_error("D1", bins=[6, 6.4, 7.0], conditions=["D1 < 7", "D1 < 8"]).set_datum({"D1": 0})
        self.assertEqual(fes._data[fes._data["D1"] == 6.2]["energy"].values[0], 0)

        fes = self.landscape.get_reweighted_line_with_walker_error("D1", bins=10, conditions=["D1 < 7", "D1 < 8"]).set_datum({"D1": 0})
        data = fes.get_data().round(4)
        self.assertTrue(type(data) == pd.DataFrame)
        self.assertTrue(data['D1'].iloc[2] == 6.3497)
        self.assertTrue(data['energy'].iloc[6] == 12.3549)
        self.assertTrue(data['energy_err'].iloc[1] == 1.2448)


class TestFreeEnergySpaceBiasExchange(unittest.TestCase):

    def setUp(self):

        self.hills = ['./test_trajectories/ndi_bias_exchange/HILLS.0',
                     './test_trajectories/ndi_bias_exchange/HILLS.1',
                     './test_trajectories/ndi_bias_exchange/HILLS.2',
                     './test_trajectories/ndi_bias_exchange/HILLS.3']

        self.landscape = FreeEnergySpace.from_standard_directory('./test_trajectories/ndi_bias_exchange/', hills_file=self.hills, verbose=False)

    def test_attributes(self):
        """
        Test the attributes of a FreeEnergySpace object
        """
        self.assertTrue(self.landscape.cvs == ['D1', 'CM1', 'CM2', 'CM3'])
        self.assertTrue(self.landscape.dt == 0.0004)
        self.assertTrue(self.landscape.max_time == 0.0596)
        self.assertTrue(self.landscape.n_timesteps == 149)
        self.assertTrue(self.landscape.opes is False)
        self.assertTrue(self.landscape.temperature == 298)

    def test_get_hills_figures(self):
        """
        Test the get_hills_figures method for a FreeEnergySpace object
        """
        figures = self.landscape.get_hills_figures()
        self.assertTrue(self.landscape._biasexchange is True)
        self.assertEqual(len(figures), 4)

        figure = self.landscape.get_average_hills_figure()
        self.assertTrue(type(self.landscape) == FreeEnergySpace)

        figure = self.landscape.get_max_hills_figure()
        self.assertTrue(type(self.landscape) == FreeEnergySpace)

        figures = self.landscape.get_hills_figures(height_power=0.5)
        self.assertTrue(self.landscape._biasexchange is True)
        self.assertEqual(len(figures), 4)

    def test_get_CM1_data(self):
        """
        Test the get_data method for a FreeEnergySpace object
        """
        data = self.landscape.lines['CM1'].get_data()
        self.assertTrue(type(data) == pd.DataFrame)

