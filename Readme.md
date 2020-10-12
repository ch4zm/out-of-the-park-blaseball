# Out of the Park Blaseball

This repo contains materials and instructions for modifying Out of the Park
to generate Underleague Blaseball leagues with much weirder team names
and player names.

## Background

Out of the Park (OOTP) is a baseball simulation video game that simulates many
off-the-field dimensions of a team (lineups, trades, free agents, contracts,
financials, etc.).

OOTP ships with a very, very long list of first/last names, grouped by different
ethnicities and with frequency distributions. It also has information about different
cities, states, and countries around the world, so that it can pick major cities for
teams and pick random cities for players' home towns.

## Overview of Customization

We will modify two folders in the OOTP application data.

The first is the `database/` folder, located at:

```
~/Library/Application Support/Out of the Park Developments/OOTP Baseball 20/database
```

This database folder contains the first names, last names, world map,
team names, and some other files we won't be modifying (historical player
and team data).

The second is the `logos/` folder, located at 

```
~/Library/Application Support/Out of the Park Developments/OOTP Baseball 20/logos
```

This folder contains the team logos, along with jersey and ballcap designs.

## Quick Start

This quick start will copy all the necessary files in this repo into OOTP
to get you going without any extra customization required on your part.

### Step 0 - Clone Repo

```
cd $HOME
git clone git@github.com:ch4zm/out-of-the-park-blaseball
cd out-of-the-park-blaseball
```

### Step 1 - Database

Note that these changes WILL break non-fantasy league baseball, so it's important
to back up the existing databases folder before making these modifications.

Copy the original database folder from `database` to `database.orig`

```
OOTPDIR="${HOME}/Library/Application Support/Out of the Park Developments/OOTP Baseball 20"
cp ${OOTPDIR}/database{,.orig}
```

Now we're going to copy some files from this repository into the `database/` folder:

```
cd $HOME/out-of-the-park-blaseball
cp database/*.{txt,xml} ${OOTPDIR}/database/.
```

That'll copy our custom first names, last names, team names, and world geography into
the game's database.

### Step 2 - Logos

OOTP is capable of generating some decent team logos by default using a set of templates,
but these aren't very exciting. Alternatively, you can create logos that correspond to a given
team nickname or team location. OOTP has a pretty sophisticated setup for creating logos and
color schemes so here's a brief rundown of the folders inside
`~/Library/Application Support/Out of the Park Developments/OOTP Baseball 20`:

* `logos/` is a folder containing logos for actual, real teams - combined city name and team nickname

* `logos/nicknames` is a folder of logos with the corresponding team nickname in their filename;
  for example, any team named the Arsonists would be assigned the default team logo `arsonists.png`
  in this folder.

* `logos/cities` is a folder of logos with the corresponding city in their filename;
  for example any team from Baltimore would be assigned the default logo `baltimore.png` in this
  folder.

To use the logos in this repo, you just need to copy the logos in `logos` to the 
`logos` folder in the OOTP application data folder:

```
cp logos/nicknames/* ${OOTPDIR}/logo/nicknames/.
cp logos/cities/* ${OOTPDIR}/logo/cities/.
```

