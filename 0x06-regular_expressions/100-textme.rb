#!/usr/bin/env ruby
puts ARGV[0].scan(/\[from:\+?1\d{10,10}\]/).join()
