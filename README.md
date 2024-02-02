# Time_Summer

Keep inserting the time durations (with or without any special characters like : etc) and it will sum it up all considering following rules : 
  1. Last 2 digits represent seconds
  2. The former 2 digits (3rd,4th last) represent minutes
  3. All other former indicate hours
  4. If you do not enter preceding zeros, it will still work

eg. 
'1' = '01' = '001' = '0001' etc = 1 second
'123' = 1 minute 23 seconds
'12345' = 1 hour 23 minutes 45 seconds
'0012034567' = 1203 hours 45 minutes 67 seconds

After the above input, if in the same line, you enter * followed by integer, it will multiply the above time by the number after *

