# MANET System Simulation
# Table of contents
- [1. Introduction](#introduction)
- [2. Installation](#installation)
	- [2.1. Install Requirements](#command)	
	- [2.2. External Libraries](#lib)
- [3. Visuals](#visuals)
- [4. Pseudocode](#pseudocode)
- [5. Credits](#credits)


## Introduction <a name="introduction"></a>
This repository contains codes for simulating an `Infrastructure-less Emergency Communication System` based on Blockchain framework.

## Installation <a name="installation"></a>
This project is developed using `Pyhton`. The requirements to run this project is included in the `requirements.txt` file in the repository.
### `pip install -r requirements.txt` <a name="command"></a>
Run this command in your shell to install the required libraries.

### External Libraries <a name="lib"></a>
- [Matplotlib]
- [Networkx]

## Visuals <a name="visuals"></a>

https://user-images.githubusercontent.com/51258896/121768371-23f70180-cb73-11eb-9ba1-6f6aa5ca0f74.mp4

https://user-images.githubusercontent.com/51258896/121768515-daf37d00-cb73-11eb-9542-deced607e5da.mp4

## Pseudocode <a name="pseudocode"></a>
```
Person {

	// Initial data stored for every person
	DLT = ∅
	Position = (x,y)
	Info = UniqeID

}

Initialize(Graph G) {

	// Start
	For each Device D ∈ G.People {
	    Create-UniqeID(D)
	    Create-DLT(D)
	    Start-WiFiScan(G, D)
	}

}

Start-WiFiScan(Graph G, Person P) {

	// Searching for other devices
	Start-Timer
	Start-Scanning

	if FIND-PEOPLE-NEARBY(G) :
		SEND-REQUEST
		UPDATE-DLT(G)

	else:
		if TIME-LIMIT-EXCEEDED:
			END

		else:
			Start-Scanning	// Again

		Endif

	Endif

}

UPDATE-DLT(Graph G) {

	// Update and merge of digital ledgers
	MAX-DISTANCE = 100 ft
	DLT = ∅

	For each Device D ∈ G.People {
	    MAKE-DISJOINT-CLUSTER-SET(D)
	}

	For each path (u, v) ∈ G.Paths ordered by increasing order by DISTANCE(u, v) {
	    if FIND-CLUSTER-SET(u) ≠ FIND-CLUSTER-SET(v):	// Checking if they are already from the same cluster or not in order to avoid cycles
	    	if DISTANCE(u, v) < MAX-DISTANCE:              // Checking if they can be merged or not based on the maximum distance
	    		DLT = DLT ∪ {(u, v)}	              // Merge
	    		UNION(u, v)
	    	Endif
	    Endif
	}
	    		
	return DLT

}
```

## Credits <a name="credits"></a>
### Developer
<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
| [<img src="https://avatars.githubusercontent.com/u/51258896?v=3" width="80px;"/><br /><sub>Ramtin Ehsani</sub>](https://github.com/ramtin-ehsani)<br />[📖](https://github.com/risc-lab/MANET-Emergency-Communication-System/commits?author=ramtin-ehsani) [💻](https://github.com/risc-lab/MANET-Emergency-Communication-System/commits?author=ramtin-ehsani) |
| :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

[Matplotlib]: <https://matplotlib.org/>
[Networkx]: <https://networkx.org/>
