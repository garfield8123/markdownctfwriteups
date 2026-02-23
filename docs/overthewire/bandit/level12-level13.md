# Level 13

Bandit OverTheWire Level 13: [level 13](https://overthewire.org/wargames/bandit/bandit13.html)

## **Level Goal**


## **Walkthrough**
- Figure out how to disassemble executable files
- Figure out how the command xxd works
- Figure out the command file and what information it provides
- Figure out how to use gzip
- Figure out how to use bzip2
- Figure out how to use tar


## **level 13 Solution**
```shell
# Makes a folder in auto generated with XXX
mktemp -d /tmp/<foldername>XXX

cd /tmp/<foldername>XXX
# performs the disassemble of data.txt
xxd -r data.txt > data

# gives us a hint of the use of gzip
file data
cp data data2.gz
gzip -d data2.gz

# gives us a hint of the use of bzip2
file data2
cp data2 data3.bz
bzip2 -d data3.bz

file data3
cp data3 data4.gz
gzip -d data4.gz

# gives us a hint of the use of tar
file data4
cp data4 data5.tar
tar -xf data5.tar

file data5.bin
cp data5.bin data6.tar
tar -xf data6.tar

file data6.bin
cp data6.bin data7.bz
bzip2 -d data7.bz

file data7
cp data7 data8.tar
tar -xf data8.tar

file data8.bin
cp data8.bin data9.gz

file data9
# ASCII text
cat data9
```

or copy paste this script

```shell
xxd -r data.txt > data1
for ((i=1; i<=10;i++)); do
    output=$(file "data$i")
    echo "$output" | grep -q "gzip" 
    if [ $? -eq 0 ]; then
        cp "data$i" "data$((i+1)).gz"
        gzip -d "data$((i+1)).gz"
    else
        echo ""
    fi
    echo "$output" | grep -q "bzip2" 
    if [ $? -eq 0 ]; then
        cp "data$i" "data$((i+1)).bz"
        bzip2 -d "data$((i+1)).bz"
    else
        echo ""
    fi
    echo "$output" | grep -q "tar" 
    if [ $? -eq 0 ]; then
        cp "data$i" "data$((i+1)).tar"
        tar -xf "data$((i+1)).tar"
        mv "data$((i+1)).bin" "data$((i+1))"
    else
        echo ""
    fi
    echo "$output" | grep -q "ASCII text"
    if [ $? -eq 0 ]; then
        cat "data$i"
    else
        echo ""
    fi
done
```

## **Generated password for level 13**
FO5dwFsc0cbaIiH0h8J2eUks2vdTDwAn
