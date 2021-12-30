import os
import tempfile

from pytemplate import main


def test_netmask_to_bit_length():
    res = main.netmask_to_bit_length('255.255.255.0')
    assert res == 24


def test_wildcard_mask_to_netmask():
    res = main.wildcard_mask_to_netmask('0.0.0.255')
    assert res == '255.255.255.0'


def test_add_ip_address():
    res = main.add_ip_address('192.168.0.1', 1)
    assert res == '192.168.0.2'


def test_load_excel_data(shared_datadir):
    file = shared_datadir / '地市配置信息表.xlsx'
    g = main.ExcelDataGenerator()

    for ds in g.load_generator(file, key='ds'):
        ds['sf_dr2_sub_iface_id'] = int(ds['sf_dr1_sub_iface_id']) - 100
        # 地市bgp宣告的网段掩码， 通过acl SC 的反掩码得到
        ds['ds_bgp_network_mask'] = main.wildcard_mask_to_netmask(
            ds['ds_acl_sc_wildcard_mask'])
        # 地市bgp宣告网段的掩码长度
        ds['ds_bgp_network_prefix'] = main.netmask_to_bit_length(
            ds['ds_bgp_network_mask'])

    assert 'SX' in g._data.keys()
    assert g._data['SX']['ds_bgp_network_prefix'] == 19


def test_load_excel_data2(shared_datadir):
    file = shared_datadir / '地市配置信息表.xlsx'
    g = main.ExcelDataGenerator()

    for col in g.load_generator(file, key='ds'):
        col['sf_dr2_sub_iface_id'] = int(col['sf_dr1_sub_iface_id']) - 100
        # 地市bgp宣告的网段掩码， 通过acl SC 的反掩码得到
        col['ds_bgp_network_mask'] = main.wildcard_mask_to_netmask(
            col['ds_acl_sc_wildcard_mask'])
        # 地市bgp宣告网段的掩码长度
        col['ds_bgp_network_prefix'] = main.netmask_to_bit_length(
            col['ds_bgp_network_mask'])

    assert 'SX' in g._data.keys()
    assert g._data['SX']['ds_bgp_network_prefix'] == 19


def test_load_template(shared_datadir):
    file = shared_datadir / '配置流程_通用版.md'
    template_str = main.load_template(file)

    assert 'telnet' in template_str


def test_write_file(shared_datadir):
    file = shared_datadir / '地市配置信息表.xlsx'
    g = main.ExcelDataGenerator()

    for ds in g.load_generator(file):
        ds['sf_dr2_sub_iface_id'] = int(ds['sf_dr1_sub_iface_id']) - 100
        # 地市bgp宣告的网段掩码， 通过acl SC 的反掩码得到
        ds['ds_bgp_network_mask'] = main.wildcard_mask_to_netmask(
            ds['ds_acl_sc_wildcard_mask'])
        # 地市bgp宣告网段的掩码长度
        ds['ds_bgp_network_prefix'] = main.netmask_to_bit_length(
            ds['ds_bgp_network_mask'])

    file = shared_datadir / '配置流程_通用版.md'
    template_str = main.load_template(file)

    with tempfile.TemporaryDirectory() as tmpdir:
        for ds, info in g._data.items():
            main.write_template(
                template_str, os.path.join(tmpdir, f'{ds}.md'), info)

            assert os.path.exists(os.path.join(tmpdir, f'{ds}.md'))


def test_not_yield(shared_datadir):
    file = shared_datadir / '地市配置信息表.xlsx'
    g = main.ExcelDataGenerator()
    g.load(file, key='ds')

    assert 'SX' in g._data.keys()
