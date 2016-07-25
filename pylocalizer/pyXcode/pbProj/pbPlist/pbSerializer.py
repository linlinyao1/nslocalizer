# Copyright (c) 2016, Samantha Marshall (http://pewpewthespells.com)
# All rights reserved.
#
# https://github.com/samdmarshall/pylocalizer
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# 1. Redistributions of source code must retain the above copyright notice, this
# list of conditions and the following disclaimer.
#
# 2. Redistributions in binary form must reproduce the above copyright notice,
# this list of conditions and the following disclaimer in the documentation and/or
# other materials provided with the distribution.
#
# 3. Neither the name of Samantha Marshall nor the names of its contributors may
# be used to endorse or promote products derived from this software without
# specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED.
# IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
# LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR
# OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
# OF THE POSSIBILITY OF SUCH DAMAGE.

from __future__ import print_function
import sys

class PBSerializer(object):

    def __init__(self, file_path=None, encoding=None, file_type=None):
        self.string_encoding = encoding
        self.file_path = file_path
        self.file_type = file_type

    def write(self, obj=None):
        if self.file_type == 'ascii':
            try:
                file_descriptor = open(self.file_path, 'w')
                self.__writeObject(file_descriptor, obj)
                file_descriptor.close()
            except IOError as exception:
                print('I/O error({0}): {1}'.format(exception.errno, exception.strerror))
            except:
                print('Unexpected error:'+str(sys.exc_info()[0]))
                raise
        else:
            import plistlib
            plistlib.writePlist(obj, self.file_path)

    def __writeObject(self, file_descriptor=None, obj=None):
        if file_descriptor is None:
            message = 'Fatal error, file descriptor is None'
            raise TypeError(message)
        if self.string_encoding is not None:
            file_descriptor.write('// !$*'+self.string_encoding+'*$!\n')
        if obj is not None:
            write_string, indent_level = obj.writeString()
            file_descriptor.write(write_string)
