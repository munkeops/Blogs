---
layout: post
title: "ML/AI based cart Conversion"
author: munkeops
categories: [internship,python,nids]
image: assets/images/digitalfootprint.png
featured: false
hidden: false
---

# ZeekDoc
 
 <p align="center">
  <img src=/Documentation/zeekLogo.png width=100>
 </p>
 

## Bro/Zeek 

### What is Zeek?

Zeek is a network analysis and IDS tool. It is an alternative to various other tools such as Snort, Suricata and OSSEC. While Snort,Suricata and Zeek to quite an extent are majorly used to perform Netwprk based IDS(NIDS) tools like OSSEC are used for Host based IDS(HIDS- such as antivirus, firewall etc).further more most IDS are generally broadly categorized into two types. The signature type or the anomaly detection type, are the two primary detection techniques. The signature type's strategy is to analyse the network traffic for predefined patterns or signatures and then raises alerts when detected where as the anomaly detection type works on listening to the network carefully and detecting any strange behaviour. The chances of a false positive are much higher in anomaly based detection but also conversely leaves room for newer attacks to happen without the signature based IDS even knowing. 
<br> Read more in the documentation : https://docs.zeek.org/en/current/intro/index.html#overview

### Why Zeek?

Unlike many other IDS such as Snort and Suricata, Zeek is a hybrid of both anomaly and rule based techniques. Zeek engine structure is indeed very efficient and useful as it creates incoming traffic into a series of events which can be either treated or left as is. An event could be anything like a a new connection , a new ssh connection or anything. The real power of Zeek comes with the Policy Script interpreter. This engine has its own scripting language (Bro/Zeek scripts eg anomaly.zeek) which comes with its own custom made data types and data structures tailored for the use of dealing with network data. Hence Zeek is able to give huge control and power to the user to be able to analyse the data in ways which would have proven very difficult before making it a decent choice to be used as an HIDS too. The user can now generate custom rules and notifications for any particular scenario and so doesent have to rely on predefined rules. Zeek can mimic anything that the conventional rules based IDS such as Snort and Suricata can do with the added advantage of customisability. A network activity in one subnet may be deemed illegal while not in another, this is where Zeek plays its trump card.
<br><br>
Now Zeek is not just merely an IDS, due to its powerful scripting nature it can be used to perform various complex tasks such as incident response, forensics, file extraction, and hashing among other capabilities. Due to its Policy engine we can provide custom scripts to perform certain operations on incoming traffic at any time. Zeek is a logging based IDS, that means it provides log files with well documented extraction data from the network activity which can be used for forensics in the term that some activity occured. The user can also write custom scripts to log additional computed information or specific parts of the connection based on the given script.
<br> Further more features as per official documentation : https://docs.zeek.org/en/current/intro/index.html#features
<br><br>

Further useful links to know more about zeek:
<br>https://zeek.org/
<br>https://www.admin-magazine.com/Archive/2014/24/Network-analysis-with-the-Bro-Network-Security-Monitor
<br>https://bricata.com/blog/what-is-bro-ids/ (very informative website with further links)
<br>http://www.iraj.in/journal/journal_file/journal_pdf/3-27-139087836726-32.pdf <br>a research paper that displays a brief comparison and uses of various IDS



