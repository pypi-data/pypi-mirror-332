{ MP_ROM_QSTR(MP_QSTR_WLAN), MP_ROM_PTR(&esp_network_wlan_type) },
{ MP_ROM_QSTR(MP_QSTR_phy_mode), MP_ROM_PTR(&esp_network_phy_mode_obj) },
{ MP_ROM_QSTR(MP_QSTR_ipconfig), MP_ROM_PTR(&esp_network_ipconfig_obj) },

{ MP_ROM_QSTR(MP_QSTR_STA_IF), MP_ROM_INT(STATION_IF)},
{ MP_ROM_QSTR(MP_QSTR_AP_IF), MP_ROM_INT(SOFTAP_IF)},

{ MP_ROM_QSTR(MP_QSTR_STAT_IDLE), MP_ROM_INT(STATION_IDLE)},
{ MP_ROM_QSTR(MP_QSTR_STAT_CONNECTING), MP_ROM_INT(STATION_CONNECTING)},
{ MP_ROM_QSTR(MP_QSTR_STAT_WRONG_PASSWORD), MP_ROM_INT(STATION_WRONG_PASSWORD)},
{ MP_ROM_QSTR(MP_QSTR_STAT_NO_AP_FOUND), MP_ROM_INT(STATION_NO_AP_FOUND)},
{ MP_ROM_QSTR(MP_QSTR_STAT_CONNECT_FAIL), MP_ROM_INT(STATION_CONNECT_FAIL)},
{ MP_ROM_QSTR(MP_QSTR_STAT_GOT_IP), MP_ROM_INT(STATION_GOT_IP)},

{ MP_ROM_QSTR(MP_QSTR_MODE_11B), MP_ROM_INT(PHY_MODE_11B) },
{ MP_ROM_QSTR(MP_QSTR_MODE_11G), MP_ROM_INT(PHY_MODE_11G) },
{ MP_ROM_QSTR(MP_QSTR_MODE_11N), MP_ROM_INT(PHY_MODE_11N) },

{ MP_ROM_QSTR(MP_QSTR_AUTH_OPEN), MP_ROM_INT(AUTH_OPEN) },
{ MP_ROM_QSTR(MP_QSTR_AUTH_WEP), MP_ROM_INT(AUTH_WEP) },
{ MP_ROM_QSTR(MP_QSTR_AUTH_WPA_PSK), MP_ROM_INT(AUTH_WPA_PSK) },
{ MP_ROM_QSTR(MP_QSTR_AUTH_WPA2_PSK), MP_ROM_INT(AUTH_WPA2_PSK) },
{ MP_ROM_QSTR(MP_QSTR_AUTH_WPA_WPA2_PSK), MP_ROM_INT(AUTH_WPA_WPA2_PSK) },
