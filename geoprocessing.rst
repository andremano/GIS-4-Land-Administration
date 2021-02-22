Geoprocessing
=============

Geoprocessing refers to methods employed to extract information and insights from an initial set of datasets. This exercise explores some of these methods.

Overlays
--------

Overlay analysis combines two or more datasets and applies a certain procedure for the common areas (those that intersect) and a different procedure for the non common areas (those that are disjoint).

.. admonition:: Resources

   This exercise uses the same dataset used for the *Spatial relationships. If you need to download the data again just clik on `this link <https://github.com/andremano/GIS-4-Land-Administration/blob/master/_static/datasets/dorset_cadaster.zip/>`_. The dataset contains the following layers:

   - *dorset_cadaster.qgz* a QGIS project preloading a *geopackage* containing the following layers:

      - *roads* (road network)
      - *water_plan* (area a water management plan where special provisions may apply)
      - *power_cable_(plan)* (proposed route for a high voltage aereal cable)
      - *parcels* (the cadaster)
      - *land_use* (land uses as of 2015)
      - *parish* (admninistrative boundary of the parishes within the Dorset municipality - Tasmania)
      - *party* (fictional list of parties)
      - *building* (empty layer of type polygon)
      - *topographic_map* (a sample topographic map generated from Open Street Map)
      - *building_type* (fictional list of types of buildings)

    In additon to the project and respective datasets, there are also folders with auxiliary files the exercise may refer to.


1. **Task** From the ``Processing toolbox``, search for tools to perform overlay operations to answer the following questions:

            * Extract the locations where the ``roads`` will be intersecting with the ``power_cable_(plan)`` *[hint: check the* ``Line intersections`` *tool]*;


            * Extract the area of the ``parish`` that is not restricted by the ``water_plan`` *[hint: check the* ``Difference`` *tool]*;


            * Extract the area of the ``water_plan`` that is not overlaps the ``parish`` *[hint: check the* ``Difference tool`` *tool]*;


            * Extract the non overlapping areas of ``water_plan`` and ``parish`` *[hint: check the* ``Symmetrical difference`` *tool]*;


            * Extract the ``parcels`` according with the boundary of the ``water_plan`` *[hint: check the* ``clip`` *tool]*.


Geometry operations
-------------------

Geometry operations usually operate on one single dataset constructing a new geometry from it.

2. **Task** From the ``Processing toolbox``, search for tools to perform geometry operations to to obtain these new layers:

            * Extract the areas within 25m from where the ``power_cable_(plan)`` *[hint: check the* ``Buffer`` *tool]*;


            * Extract the all the vertices from the ``parcels`` *[hint: check the* ``Extract vertices`` *tool]*;


            * Group the ``parcels`` according to the type of tenure *[hint: check the* ``Dissolve`` *tool]*.

Analysis
--------

Analysis seek to produce previously unknown information from the data we have. The next task provides an example of such analysis.

3. **Task** From the ``Processing toolbox``, search for tools to perform geometry operations to to obtain these new layers:

            * Extract the areas within 25m from where the ``power_cable_(plan)`` *[hint: check the* ``Buffer`` *tool]*;

Challenge
---------

You can combine these tools and obtain answers to complicated problems. Read the problem formulation and try to come up with a solution using one or more of the tools you experimented so far.

*The* ``power_cable_plan`` *represents the proposed route for a necessary high voltage connection. It is still under discussion and as an input for that discussion you are asked to determine how much land per* ``parcel`` * would have to be expropriated given that around each post a 10m security area is required by law*

[**hint:** you will need to use the ``Extract vertices``, the ``Buffer`` and the ``Overlap analysis`` tools.