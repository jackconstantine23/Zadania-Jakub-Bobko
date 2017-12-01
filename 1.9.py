input_file = 'nazwa_pliku.txt';
output_file = 'output.txt';
delete_list = ['się','i','oraz','nigdy','dlaczego'];
fin = open(input_file);
read_lines = [];
changed_lines = [];
for line in fin: 
    for word in line.split():
        if word in delete_list:
            line = line.replace(word,"");
    read_lines.append(line);
fin.close();

fout = open(output_file,'w+');
for line in read_lines:
    fout.write(line);
fout.close();
