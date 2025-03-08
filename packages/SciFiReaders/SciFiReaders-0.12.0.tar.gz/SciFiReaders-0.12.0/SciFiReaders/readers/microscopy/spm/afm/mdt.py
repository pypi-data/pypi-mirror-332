
#The following code have been particularly copied from the https://github.com/symartin/PyMDT

import numpy as np
import sidpy
import sidpy as sid
from sidpy.sid import Reader
import io
from struct import *
import xml.etree.ElementTree as ET


#Decarator has been copied from the https://github.com/symartin/PyMDT

class MDTBufferedReaderDecorator(object):
    """
        A decorator class that facilitate the sequential reading of a file.

        The class will redirect al the standard file methods and add some methods to read and integer and float number
        encoded on 8, 16, 32 or 64 bits
    """

    def __init__(self, file_):
        self._file = file_

    def shift_position(self, shift_bytes):
        self._file.seek(shift_bytes, io.SEEK_CUR)

    def read_uint8(self):
        """Read a unsigned integer coded on 1 byte (a char)"""
        return unpack("<B", self._file.read(1))[0]

    def read_uint16(self):
        """Read a unsigned integer coded on 2 byte (a short)"""
        return unpack("<H", self._file.read(2))[0]

    def read_uint32(self):
        """Read a unsigned integer coded on 4 byte (a usual int or long int)"""
        return unpack("<I", self._file.read(4))[0]

    def read_uint64(self):
        """Read a unsigned integer coded on 8 byte (a long long)"""
        return unpack("<Q", self._file.read(8))[0]

    def read_int8(self):
        """Read a signed integer coded on 1 byte (a char)"""
        return unpack("<b", self._file.read(1))[0]

    def read_int16(self):
        """Read a signed integer coded on 2 byte (a short)"""
        return unpack("<h", self._file.read(2))[0]

    def read_int32(self):
        """Read a unsigned integer coded on 4 byte (a usual int or long int)"""
        return unpack("<i", self._file.read(4))[0]

    def read_int64(self):
        """Read a unsigned integer coded on 8 byte (a long long)"""
        return unpack("<q", self._file.read(8))[0]

    def read_char(self):
        """Read one character coded on 1 byte (a usual char)"""
        return unpack("<c", self._file.read(1))[0]

    def read_uchar(self):
        """Read a unsigned integer coded on 1 byte (a char)
            idem that read_uint8()
        """
        return int(unpack('<B', self._file.read(1))[0])

    def read_float32(self):
        """Read a signed float coded on 4 byte (a float)"""
        return float(unpack('<f', self._file.read(4))[0])

    def read_float64(self):
        """Read a signed float coded on 8 byte (au double float)"""
        return float(unpack('<d', self._file.read(8))[0])

    def extract_string(self, string_len):
        string_bytes = self._file.read(string_len)
        # i don't really know why but decode('utf-8) does't work for '°'
        return "".join(map(chr, string_bytes))

    def __getattr__(self, attr):
        return getattr(self._file, attr)

class MDTReader(Reader):
    """
        Extracts data and metadata from NT-MDT (.mdt) binary files containing
        images or curves.

    """

    def __init__(self, file_path, *args, **kwargs):
        super().__init__(file_path, *args, **kwargs)

    def read(self, verbose=False):
        '''
        Reads the file given in file_path into a list of sidpy dataset

        Returns
        -------
        sidpy.Dataset : List of sidpy.Dataset objects.
            Multi-channel inputs are separated into individual dataset objects
        '''
        self._file = MDTBufferedReaderDecorator(open(self._input_file_path, mode='rb'))

        #read header of the file
        self._read_header()

        if verbose:
            print(f'File size: {self._file_size}')
            print(f'Number of frames: {self.nb_frame}')
            print()
        dataset_dict = {}
        #channel_number = 0
        #iterator for the frames inside the file
        for i in range(self.nb_frame):
            self._frame = Frame(decorator = self._file)

            # 2d scan
            if self._frame.type == 106:
                self._frame._read_mda_frame()
            #curves_new: point cloud, spectra
            elif self._frame.type == 190:
                self._frame._read_point_cloud()
            #text
            else:
                #self._frame.type == 3:
                self._frame._read_text()#TODO


            #dataset_list.append(self._frame.data)
            key_channel = f"Channel_{i:03d}"
            dataset_dict[key_channel] = self._frame.data

            #might be rewrite to create dict() initially - without list()
            # dataset_dict = {}
            # for index, dataset in enumerate(dataset_list):
            #     if type(dataset) == sidpy.Dataset:
            #         title = dataset.title
            #     elif type(dataset) == dict:
            #         title = 'Spectral_data'
            #     else:
            #         title = 'Unknown'
            #
            #     dataset_dict[f'{index:03}_{title}'] = dataset

            if verbose:
                print(f'Frame #{i}: type - {self._frame.type}',
                      f'start_position - {self._frame.start_pos},')
                if (self._frame.type == 106) or (self._frame.type == 190):
                    print(f'title - {self._frame.title}',
                          f'version - {self._frame.version}, '
                          f'time - {self._frame.date}, '
                          f'uuid - {self._frame.uuid}')
                print('\n')

        self._file.close()

        return dataset_dict

    def _read_header(self):
        '''

        Read of the header of MDT file contained information about a number of frames (self.nb_frame)
        and file size (self._file_size)

        '''
        # magic header
        self._file.shift_position(4)

        # File frm_byte_size (w/o header)
        self._file_size = self._file.read_uint32()

        #  4 bytes reserved (??)
        self._file.shift_position(4)

        # last frame
        self.nb_frame = self._file.read_uint16() + 1 #it originally returns number of frame -1, due to numeration from zero

        #  19 bytes reserved (??)
        self._file.shift_position(19)

class Frame:
    '''
    Class for MDA frames
    '''
    def __init__(self, decorator=None):
        self._file = decorator
        self.MDT_data_types = {-1: self._file.read_int8,
                               1: self._file.read_uint8,
                               -2: self._file.read_int16,
                               2: self._file.read_uint16,
                               -4: self._file.read_int32,
                               4: self._file.read_uint32,
                               -8: self._file.read_int64,
                               8: self._file.read_uint64,
                               -5892: self._file.read_float32,
                               -13320: self._file.read_float64}
        self._read_frame_header()
        self.metadata = {'date': self.date,
                         'version': self.version,}


        #TODO how to extract one frame without iteration?

    def _read_frame_header(self):

        '''Extract data common for all type of frames'''

        self.start_pos = self._file.tell()
        self.size = self._file.read_uint32()
        self.type = self._file.read_uint16()
        # frame version
        _version_minor = self._file.read_uint8()
        _version_major = self._file.read_uint8()
        self.version = _version_major + _version_minor*1e-1
        # date and time
        _year = self._file.read_uint16()
        _month = self._file.read_uint16()
        _day = self._file.read_uint16()
        _hour = self._file.read_uint16()
        _min = self._file.read_uint16()
        _sec = self._file.read_uint16()
        self.date = f'{_month}/{_day}/{_year} {_hour}:{_min}:{_sec}'

        self.var_size = self._file.read_uint16()

    def _read_mda_frame(self):
        '''read mda frame'''

        #skip frame header
        self._file.seek(self.start_pos+22)

        _head_size = self._file.read_uint32()
        _total_length = self._file.read_uint32()

        #read_uuid
        _bin_uuid = []
        for _ in range(16):
            _bin_uuid.append( self._file.read_char())
        self.uuid = self.restore_guid(_bin_uuid)
        self.metadata['uuid'] = self.uuid

        #uuid is written 2 times
        self._file.shift_position(16)

        # skip 4 empty bytes
        self._file.shift_position(4)

        #size of name and xml
        _name_size  = self._file.read_uint32()
        _xml_size   = self._file.read_uint32()
        #some metrics
        _info_size  = self._file.read_uint32()
        _spec_size  = self._file.read_uint32()
        _source_info_size = self._file.read_uint32()
        _var_size = self._file.read_uint32()
        _data_offset = self._file.read_uint32()
        _data_size = self._file.read_uint32()

        #extract metadata and title
        if _name_size !=0:
            self.title = self._file.read(_name_size).decode('utf-8')
        if _xml_size != 0:
            xml_metadata = self._file.read(_xml_size).decode('utf-16')
            #original metadata
            element = ET.fromstring(xml_metadata)
            original_metadata = self.xml_to_dict(element)

        #don't understand self.info, self.spec, self.source_info
        if _info_size != 0:
            self.info = self._file.read(_info_size)
        if _spec_size != 0:
            self.spec = self._file.read(_spec_size)
        if _source_info_size != 0:
            self.source_info = self._file.read(_source_info_size)

        #skip _var_size
        self._file.shift_position(4)


        _struct_len = self._file.read_uint32()
        _current_pos = self._file.tell()
        _array_size = self._file.read_uint64()
        _cell_size = self._file.read_uint32()

        self.n_dimensions = self._file.read_uint32()
        self.n_measurands = self._file.read_uint32()

        self._file.seek(_struct_len + _current_pos)

        if self.n_dimensions > 0:
            self.dimensions = []
            for _ in range(self.n_dimensions):
                self.dimensions.append(self._read_mda_calibrations())

        if self.n_measurands > 0:
            self.measurands = []
            for _ in range(self.n_measurands):
                self.measurands.append(self._read_mda_calibrations())

        if self.n_dimensions == 2 and self.n_measurands == 1:
            self.data = self._extract_2d_frame()
            #self.data.type = '2D IMAGE'

        self.data.metadata = self.metadata
        self.data.original_metadata = original_metadata
        self.data.title = self.title

        self._file.seek(self.start_pos + self.size)

    def _read_text(self):
        #TODO
        self.data = None
        self._file.seek(self.start_pos + self.size)

    def _read_maps(self):
        """
        read scanned data (maps of curves)
        """
        self._file.seek(self.start_pos + 22)

        self.data = None
        self._file.seek(self.start_pos + self.size)

    def _read_point_cloud(self):
        """
        '''
        Extract data from spectroscopy map

        Returns
        -------
        list:  sidpy.Dataset objects
        '''
        """
        # parm_dict = {'date': self.date,
        #              } #dictionary for metadata

        self._file.seek(self.start_pos + 22)
        #read numer of blocks with data
        _block_count = self._file.read_uint32()

        #read blocks headers: (name length, length, length from starting point)
        _block_headers = []
        _full_len = 0
        for i in range(_block_count):
            _name_len = self._file.read_uint32()
            _len      = self._file.read_uint32()
            _full_len += _len
            _block_headers.append((_name_len, _len, _full_len))

        #read block names
        _block_names = []
        for i in range(_block_count):
            _name = self._file.read(_block_headers[i][0]).decode('utf-8')
            _block_names.append(_name)

        #indexes of points blocks
        ind_points = np.array([i for i, name in enumerate(_block_names) if name[:5] == "point"])

        _current_pos = self._file.tell()

        #calibration for points, calibration for data in each curve in points, and calibrations for x axis
        self.calibr_p, self.calibr_d, self.calibr_ax, self.calibr_m = self._read_curves_new_calibrations(_block_names, _block_headers)
        self.metadata['uuid'] = self.uuid

        #finding  positions: xreal, yreal
        self.x_real, self.y_real = self._read_curves_new_xreal_yreal()
        #extract passes, directions, axes
        self.passes, self.inverse, self.axes, self.meas = self._read_curves_new_array_params()


        self.point_data_indexes = {} #to find points indexes corresponding data indexes
        _point_data = {} #dict for spectroscopic data
        #extract z data for all points
        for num,i in enumerate(ind_points):
            if i > 0:
                self._file.shift_position(_block_headers[i-1][2])
            _header = _block_headers[i]
            _ind_data = []
            #read number of data files corresponding to this point
            for _ in range(_header[1]//4):
                _ind_data.append(self._file.read_uint32())

            self.point_data_indexes[int(_block_names[i][5:-4])] = _ind_data #save curve indexes for each point
            _ind_for_sort = []#searching corresponded calibrations

            for ind in _ind_data:
                indd = _block_names.index(f'data{ind}.dat') #real index or the data block

                # return to the start position of the block
                self._file.seek(_current_pos)
                if indd > 0:
                    self._file.shift_position(_block_headers[indd-1][2])
                _header_data = _block_headers[indd]
                _dat_el = np.array([])
                for _ in range(_header_data[1]//8):
                    _dat_el = np.append(_dat_el, self._file.read_float64())
                #reverse backward pass
                # if self.calibr_d[ind][1] == 0: #TODO which one we should reverse?
                #     _dat_el = np.flip(_dat_el)
                _point_data[ind] = _dat_el

            self._file.seek(_current_pos)

        #here we already have
        #self.point_data_indexes - indexes of the curves in the each point
        #self.x_real, self.y_real - all all real coordinates of the points
        #self.passes, self.inverse - lists with the numbers of cycles and directions (0 - forward, 1 - backward, 2 - ?undetermined)

        # all coordinates of spectral data (real_x, real_y, cycle, direction)
        coordinate = np.array(list(self.calibr_p.values()))[:,:-1].astype('float')

        #add points coordinates to the metadata
        self.metadata['coordinates'] = coordinate

        _arrays = {}
        _key_dict = {} #to store correspondence between _key and axes
        #create dictionary with zeros sidpy arrays for each map
        for aa, _x_key in enumerate(self.calibr_ax):
            _x_dim = self.calibr_ax[_x_key]
            _key_dict[_x_key] = {}
            for mm,_y_key in enumerate(self.calibr_m):
                _y_dim = self.calibr_m[_y_key]
                _n = aa * len(self.calibr_m) + mm
                _key = f'{_n:03}_{_y_dim[0]}({_x_dim[3]})'
                _key_dict[_x_key][_y_key] = _key
                _arrays[_key] = np.zeros([len(self.point_data_indexes.keys()),
                                          len(self.passes),
                                          len(self.inverse),
                                          _x_dim[2],])

        #fill the arrays
        for point_number in self.point_data_indexes.keys():
            for curve_number in self.point_data_indexes[point_number]:
                _pass      = self.calibr_d[curve_number][0]
                _direction = self.calibr_d[curve_number][1]
                _direction = 0 if _direction == 2 else _direction
                #restore key of array
                _axis = self.calibr_d[curve_number][2]
                _meas = self.calibr_d[curve_number][3]
                _key = _key_dict[_axis][_meas]
                _arrays[_key][point_number, _pass, _direction] = _point_data[curve_number]

        self.arrays = _arrays

        for _axis in _key_dict:
            for _meas in _key_dict[_axis]:
                _key = _key_dict[_axis][_meas]
                _x_axis, _y_axis = self.calibr_ax[_axis], self.calibr_m[_meas]
                _x_data = np.linspace(_x_axis[0], _x_axis[1], _x_axis[2])
                #joint "direction dimension" and squeeze array
                if len(self.inverse) == 2:
                    _x_data = np.append(_x_data, np.flip(_x_data))
                    _arrays[_key] = np.append(_arrays[_key][:, :, 0], _arrays[_key][:, :, 1], axis=2)
                _arrays[_key] = np.squeeze(_arrays[_key])

                #build sidpy array
                _data_set = sid.Dataset.from_array(_arrays[_key], name=_key)

                if len(self.point_data_indexes) == 1:
                    _data_set.data_type = 'spectrum'
                else:
                    _data_set.data_type = 'point_cloud'

                dn = 0 #dimention number
                # 1) point cloud dimention
                point_list = list(self.point_data_indexes)
                if len(point_list) > 1:
                    _data_set.set_dimension(dn, sid.Dimension(list(self.point_data_indexes),
                                                              name='point_number',
                                                              quantity='Point number',
                                                              dimension_type='point_cloud'))
                    dn +=1

                if len(self.passes) > 1:
                    _data_set.set_dimension(dn, sid.Dimension(self.passes,
                                                              name='pass',
                                                              quantity='Pass',
                                                              dimension_type='channel'))
                    dn += 1

                _data_set.set_dimension(dn, sid.Dimension(_x_data,
                                                          name=_x_axis[-2],
                                                          units=_x_axis[-1],
                                                          quantity=_x_axis[-2],
                                                          dimension_type='spectral'))
                _data_set.units = _y_axis[1]
                _data_set.quantity = _y_axis[0]
                _data_set.metadata = self.metadata
                _data_set.original_metadata = self.original_metadata
                _data_set.title = _key

                _arrays[_key] = _data_set
        if len(_arrays) == 1:
            self.data = list(_arrays.values())[0]
            self.data.title = self.title
        else:
            self.data = _arrays
        #self.data.title = self.title


        self._file.seek(self.start_pos + self.size)

    def _read_curves_new_calibrations(self, _block_names, _block_headers):
        '''
        Read calibrations from the index.xml blocks

        Returns
        -------
        dict
            Calibrations for each point position: real_x, real_y, xy_unit
        dict
            Calibrations for curves (y axis): pass, direction, signal_name, signal_unit
        dict
            Calibrations for curves (x axis): start_value, stop_value, count, x_axis_name, x_axis_units
        '''
        _current_pos = self._file.tell() #just to be sure

        calibr_points = {} #Point tag in index.xml block
        calibr_data   = {} #Meas tag in index.xml block
        calibr_axis   = {} #Axis tag in index.xml block
        calibr_name   = {} #Name tag in index.xml block
        calibr_meas   = {} #part of calibr_name  representing Y axes

        #read_uuid
        _bin_uuid = []
        for _ in range(16):
            _bin_uuid.append( self._file.read_char())
        self.uuid = self.restore_guid(_bin_uuid)
        self._file.seek(_current_pos)
        #--------

        #find index.xml block position
        ind = _block_names.index('index.xml')
        self._file.shift_position(_block_headers[ind - 1][2])

        #string with xml data
        xmml = self._file.read(_block_headers[ind][1]).decode('utf-8')
        self.xml = xmml



        #parsing of index.xml string
        root = ET.fromstring(xmml)[0]
        self.version = root.attrib['version']
        #read general data about axis dimensions
        for child in root:
            if child.tag == 'Name':
                calibr_name[child.attrib['index']] = (child.attrib['name'],
                                                      child.attrib['unit'],)
        #read points, data and axis calirations
        for child in root:
            if child.tag == 'Axis':
                calibr_axis[int(child.attrib['index'])] = (float(child.attrib['start']),
                                                           float(child.attrib['stop']),
                                                           int(child.attrib['count']),
                                                           calibr_name[child.attrib['name']][0],
                                                           calibr_name[child.attrib['name']][1])
            if child.tag == 'Point':
                calibr_points[int(child.attrib['index'])] = (float(child.attrib['x']),
                                                             float(child.attrib['y']),
                                                             child.attrib['unit'])
            if child.tag == 'Meas':
                calibr_data[int(child.attrib['index'])] = (int(child.attrib['pass']),
                                                            int(child.attrib['inverse0']),
                                                            int(child.attrib['axis0']),
                                                            int(child.attrib['name']),
                                                            calibr_name[child.attrib['name']][0],
                                                            calibr_name[child.attrib['name']][1],
                                                            )
                if int(child.attrib['name']) not in calibr_meas:
                    calibr_meas[int(child.attrib['name'])] = calibr_name[child.attrib['name']]

        self._file.seek(_current_pos)

        #Extraction of metadata from the last block.
        #Actually, number of metadata blocks == number of points, but looks like they are absolutely identical
        self._file.shift_position(_block_headers[-2][2])
        xml_metadata = self._file.read(_block_headers[-1][1]).decode('utf-16')
        element = ET.fromstring(xml_metadata)
        self.original_metadata = self.xml_to_dict(element)
        self.title = self.original_metadata['Parameters']['Name']['Name']
        #original metadata

        self._file.seek(_current_pos)
        return calibr_points, calibr_data, calibr_axis, calibr_meas

    def _read_curves_new_xreal_yreal(self):
        '''Create array from real coordinated of points in curves_new'''
        xreal = []
        yreal = []
        for key in self.calibr_p.keys():
            x = self.calibr_p[key][0]
            y = self.calibr_p[key][1]
            xreal.append(x)
            yreal.append(y)

        xreal = np.array(sorted(set(xreal)))
        yreal = np.array(sorted(set(yreal)))
        return xreal, yreal

    def _read_curves_new_array_params(self):
        '''Create array with cycles numbers and directions'''
        cycles = []
        passes = []
        meas = []
        axes = []

        for dat in self.calibr_d.values():
            _c, _d, _a, _m  = dat[:-2]
            cycles.append(_c)
            passes.append(_d)
            axes.append(_a)
            meas.append(_m)

        cycles = np.array(sorted(set(cycles)))
        passes = np.array(sorted(set(passes)))
        meas = np.array(list(range(len(set(meas)))))  # meas was string list
        axes = np.array(sorted(set(axes)))

        return cycles, passes, axes, meas

    def _read_mda_calibrations(self):
        '''
        Read parameters and calibrations for mda frame

        Returns
        -------
        dict : dict with parameters
        '''
        _current_pos = self._file.tell()
        calibrations = {}

        #parameters length for further parsings
        _len_tot     = self._file.read_uint32()
        _len_struct  = self._file.read_uint32()

        _pos_after_struct = self._file.tell() + _len_struct

        _len_name    = self._file.read_uint32()
        _len_comment = self._file.read_uint32()
        _len_unit    = self._file.read_uint32()

        calibrations['si_unit'] = self._file.read_uint64()
        calibrations['accuracy'] = self._file.read_float64()
        self._file.shift_position(8)
        calibrations['bias'] = self._file.read_float64()
        calibrations['scale'] = self._file.read_float64()
        calibrations['min_index'] = self._file.read_uint64()
        calibrations['max_index'] = self._file.read_uint64()
        calibrations['data_type'] = self._file.read_int32() #signed integer
        calibrations['length'] = calibrations['max_index'] - calibrations['min_index'] + 1


        _len_author = self._file.read_uint32()

        #?
        self._file.seek(_pos_after_struct)

        if _len_name > 0:
            calibrations['name'] = self._file.extract_string(_len_name)
        if _len_comment > 0:
            calibrations['comment'] = self._file.extract_string(_len_comment)
        if _len_unit > 0:
            calibrations['unit'] = self._file.extract_string(_len_unit)
        if _len_author > 0:
            calibrations['author'] = self._file.extract_string(_len_author)

        self._file.seek(_current_pos + _len_tot)
        return calibrations

    def _extract_2d_frame(self):
        '''
        Extract data from 2d scan

        Returns
        -------
        sidpy.Dataset : 2d dataset object with AFM image data
        '''
        x = self.dimensions[1]
        y = self.dimensions[0]
        z = self.measurands[0]

        total_len = x['length'] * y['length']

        xreal = x['scale'] * (x['length'] - 1)
        yreal = y['scale'] * (y['length'] - 1)


        read_data = self.MDT_data_types[z['data_type']]

        data = np.zeros(total_len)

        #read data
        for i in range(len(data)):
            data[i] = z['bias'] + z['scale'] * read_data()

        data = np.rot90(np.reshape(data, (x['length'],y['length'])), k=3)

        # Convert it to sidpy dataset object
        data_set = sid.Dataset.from_array(data)
        data_set.title = self.title
        data_set.data_type = 'Image'

        # Add quantity and units
        data_set.units = z['unit']
        data_set.quantity = self.title.split(':')[-1]

        # Add dimension info
        data_set.set_dimension(1, sid.Dimension(np.linspace(0, xreal, x['length']),
                                                name='y',
                                                units=x['unit'], quantity='y',
                                                dimension_type='spatial'))
        data_set.set_dimension(0, sid.Dimension(np.linspace(0, yreal, y['length']),
                                                name='x',
                                                units=y['unit'], quantity='x',
                                                dimension_type='spatial'))
        return data_set

    #helper methods
    def xml_to_dict(self, element):
        result = {}
        if element.text:
            result[element.tag] = element.text
        for child in element:
            child_data = self.xml_to_dict(child)
            if child.tag in result:
                if isinstance(result[child.tag], list):
                    result[child.tag].append(child_data)
                else:
                    result[child.tag] = [result[child.tag], child_data]
            else:
                result[child.tag] = child_data
        return result

    @staticmethod
    def restore_guid(b_list):
        '''
        Restoring GUID of frame from binary list
        '''
        hex_list = [x.hex() for x in b_list]
        ind = [0, 4, 6, 8, 10, 16]
        hex_list_cor = []
        for i in range(len(ind) - 1):
            part = hex_list[ind[i]:ind[i + 1]]
            if ind[i + 1] < 10:
                part.reverse()
            str_part = ''.join(part)
            hex_list_cor.append(str_part)

        return '-'.join(hex_list_cor).upper()















