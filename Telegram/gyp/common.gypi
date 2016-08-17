# This file is part of Telegram Desktop,
# the official desktop version of Telegram messaging app, see https://telegram.org
#
# Telegram Desktop is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# It is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# In addition, as a special exception, the copyright holders give permission
# to link the code of portions of this program with the OpenSSL library.
#
# Full license: https://github.com/telegramdesktop/tdesktop/blob/master/LICENSE
# Copyright (c) 2014 John Preston, https://desktop.telegram.org

{
  'variables': {
    'variables': {
      'variables': {
        'build_os%': '<(OS)',
      },
      'build_os%': '<(build_os)',
      'conditions': [
        [ 'build_os == "win"', {
          'build_win': 1,
        }, {
          'build_win': 0,
        }],
        [ 'build_os == "mac"', {
          'build_mac': 1,
        }, {
          'build_mac': 0,
        }],
        [ 'build_os == "linux"', {
          'build_linux': 1,
        }, {
          'build_linux': 0,
        }],
      ],
    },
    'build_os%': '<(build_os)',
    'build_win%': '<(build_win)',
    'build_mac%': '<(build_mac)',
    'build_linux%': '<(build_linux)',

    # GYP does not support per-configuration libraries :(
    # So they will be emulated through additional link flags,
    # which will contain <(ld_lib_prefix)LibraryName<(ld_lib_postfix)
    'conditions': [
      [ 'build_win', {
        'ld_lib_prefix': '',
        'ld_lib_postfix': '.lib',
      }, {
        'ld_lib_prefix': '-l',
        'ld_lib_postfix': '',
      }],
    ],
    'ld_lib_prefix': '<(ld_lib_prefix)',
    'ld_lib_postfix': '<(ld_lib_postfix)',

    'library%': 'static_library',

    'official_build_target%': '<!(python <(DEPTH)/official.py --read-target)',
  },

  'configurations': {
    'Debug': {
      'defines': [
        '_DEBUG',
      ],
    },
    'Release': {
      'defines': [
        'NDEBUG',
      ],
    },
  },
}