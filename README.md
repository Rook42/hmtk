# hmtk
Rook's HackMaster Toolkit

A collection of python tools aimed at increasing speed of previously time-consuming game mastering tasks.
Assumes HackMaster 5th edition, and extends it with Rook's personal houserules.

Current development will likely consist of simple quality-of-life record keeping tasks for managing adventures.

This project's primary aim is to make previously time-intensive GM tasks faster, to save time in session preparation and to be able to afford a more immersive session experience without sacrificing flow. Many of the proposed features are aimed at speeding up HackMaster systems which otherwise might be glossed over, specifically those that make HackMaster more of a fantasy survival simulation than competing RPGs. 

Note: Any content originally by another author (K&C, TSR, etc) that finds its way into this project is the sole property of its owners, used here not for profit in a transformative manner.
This project is to be used to augment the use of the original source material, not replace it. 
Basically, buy the books, folks. Even the digital copies support the people that make the things we love, but dead trees make the game much nicer to play than screens alone. It's the original target format for the design, and they tend to look gorgeous just laying around in your house. Buy the books.

long-term goals:


Player mode with player-centric toolsets for player usecase. 
  Tools might include character management, a combat view, and ability breakdowns (spell/ability information for reference). 
  It could be nice to incorporate general notetaking about any particular entity, for example making a note of where/when an item was obtained. 
    It might be nice to be able to load objects (made by the GM) from the filesystem, to form an analogue of the GM passing a player a notecard with stats for an item, ally, or other entity that they have acquired. 
    Likewise, allowing the Player to save their character and send it to the GM would amplify the GM's access to character information while maintaining a smooth workflow. The GM could then even mark experience after a session and send the revised character sheet to the player at their leisure, or at the beginning of the next session.
 
GM mode including:
Adventure management:
  Player characters and their statuses, locations, notes, the date. Perhaps character sheet printable generation.
Random Player Character generation
Adventure/Dungeon generation
Travel immersion support:
  Supplies consumed during travel (daily, total), perhaps compared with party inventory.
  Random encounters.
  Potentially, journey storytelling quality of life improvements, such as:
    List of nearby destinations with type, distance.
    Difficulty/speed of transversing terrain.
    Random journey encounters taking location into account for possible events and likelihoods.
Setting information access / immersive setting description generation:
  Provide access to setting information (abstracted from Kingdoms of Kalamar setting books) that would otherwise be difficult to quickly reference.
  Setting-accurate calendar.
  Description generation for local area, potentially including weather.
  
Distributable  

Houserule support:
  Houserule middle ages money conversion 
    Converts any monetary amount from HM to loosely equivalent* real-world middle ages currency.
      *As Kalamar is a fictional world, there will be differences in comparative value for goods and services.
  Houserule AD&D (1/2) automatic stat conversion.
    AD&D versions one and two have a much larger content library than HackMaster. Since the underlying systems for AD&D are significantly different from HackMaster, automatic D&D asset conversion to HackMaster might allow a broader range of content for GMs to include in their campaigns.
    AD&D was chosen in preference to D20 systems (D&D 3e, etc) as it more closely resembles HackMaster tone and operations. For example, the average HackMaster player character is similar in power to a relatively anemic equivalent AD&D character of half the levels rounding down. Finding a similar equivalent for D&D 3e would be challenging, as power creep tends to happen earlier in character progression and worsens as the volume of first and third party expansions to the 3e system considered widens. A potential exception might be found in D&D 5e, but this will require examination and almost certainly provides less content-per-effort than AD&D. That said, having a more recent body of content to convert from might be beneficial.
