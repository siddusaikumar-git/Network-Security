--------------- Team 8 -----------------

Simulated Router ID's : 350 router ID to 400 router ID
Router ID's removed : 392, 394, 395, 396, 397, 398, 399, 400

------ Requirements: ------- : Configuration and Installation Instructions

To Implement Distributed Denial of Service in Mininet and Wireshark for the given/generated data, these are the requirements:
1. Install Virtual Box
2. Download Ubuntu 18.04 LTS iso image and link to Virtual Box.
3. Open Ubuntu and install mininet and Wireshark in the Home directory.
4. Copy "data.txt", "beforeAttack.py" and "afterAttack.py" to one folder in Ubuntu.

To visualize the network of given data, these are the requirements:
1. Python version 3.7 
2. Anaconda software for Jupyter Notebook or Jupyter Notebook
2. matplotlib library version 3.3.4
3. pyvis library version 0.1.9 
5. data set names as "data.txt", "wireshark_before_attack_output.csv", "wireshark_after_attack_output.csv" should be placed in the same directory as "project3.ipynb" file.


----- Execution Steps ------- : Operating Instructions

Steps to execute and Implement host to host pinging, ddos attack:
1. Open the Terminal in the Ubuntu and goto respective directory of "beforeAttack.py"/"afterAttack3.py"/"data.txt" file.
2. Open Wireshark, double click on "any" to capture the data and filter with "icmp" in the search bar.
3. Run the command in terminal as "sudo mn --custom beforeAttack.py --topo mytopo --switch lxbr,stp=1" to ping all between different hosts
   within the networks. followed by run the command "pingall" in the mininet.
4. Able to see the connections and pinging results on the command line interface, results are displayed in "before_attack_cli_output.txt"
5. Parallely able to see the Display of packets/transactions count increased in the display.
6. Once "pingall" is done, stop the capture in Wireshark, save the captured content as CSV file and .pcap file.
7. Similarly, to implement Ddos attack, run the command "sudo mn --custom afterAttack.py --topo mytopo --switch lxbr,stp=1", after "pingall",
   command line interface results are displayed in "after_attack_cli_output.txt"

Steps to execute and display average number of packets per node in network:
1. Open the file "project3.ipynb" file using Jupyter Notebook.
2. Then click on "Cell" and "Run All" option.
3. At the end of each cell you will see the nodes executed with corresponding outputs.


Note1: Each router is having only one host connected to it, but routers are connected to multiple routers as per the "data.txt"
Note2: files "wireshark_before_attack_output.csv" and "wireshark_after_attack_output.csv" have source ip's and target ip's in such a way that 
       the IP 10.0.0.1 represents 350 router, 10.0.0.2 represents 351 router, ........., 10.0.0.51 represents 400 router.

------ Other files Included:
1. before_attack.html : contains router to router connections, router size is w.r.t average number of packets per node  
2. after_attack.html  : contains router to router connections, router size is w.r.t average number of packets per node, node with red color are removed nodes.
3. wireshark_before_attack_output.pcap : wireshark output file before capturing before attack
4. wireshark_after_attack_output.pcap  : wireshark output file after capturing before attack


Team 8 -- Team Memebers (our routers range is from 350 - 400)
1. Sai Kumar Siddu -> R11779742 (Section CS5342-001)
2. Subhakari Mounika Gandham - R11789255 (Section CS5342-001)    
3. Chandana Tulluru - R11800872 (Section CS5342-001)
4. Akhil katkam - R11784414 (Section CS5342-001)
5. Muramshetti Srinivasa Chanakya  - R11803400 (Section CS5342-003)