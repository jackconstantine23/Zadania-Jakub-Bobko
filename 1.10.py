input_file = 'Zurek.txt';
output_file = 'Zurek_changed.txt';
equivalent_list= {'i':'oraz','oraz':'i','nigdy':'prawie nigdy','dlaczego':'czemu'};
fin = open(input_file);
read_lines = [];
changed_lines = []; 
for line in fin:
    for word in line.split():
        if word in equivalent_list:
            line = line.replace(word,equivalent_list[word]);
    read_lines.append(line);
fin.close();

fout = open(output_file,'w+');
for line in read_lines:
    fout.write(line);
fout.close();
