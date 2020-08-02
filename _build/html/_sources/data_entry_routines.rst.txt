Data entry routines
-------------------

.. admonition:: Resources

   This exercise uses the same dataset used for the *Spatial relationships. If you need to download the data again just clik on `this link <https://canvas.utwente.nl/courses/6395/files/1773079/download?download_frd=1/>`_. The dataset contains the following layers:

   - *dorset_cadaster.qgz* a QGIS project preloading a *geopackage* containing the following layers:

      - *roads* (road network)
      - *water_plan* (area a water management plan where special provisions may apply)
      - *power_line_project* (proposed route for a high voltage aereal cable)
      - *parcels* (the cadaster)
      - *land_use* (land uses as of 2015)
      - *parish* (admninistrative boundary of the parishes within the Dorset municipality - Tasmania)
      - *party* (fictional list of parties)
      - *building* (empty layer of type polygon)
      - *topographic_map* (a sample topographic map generated from Open Street Map)
      - *building_type* (fictional list of types of buildings)

    In additon to the project and respective datasets, there are also folders with auxiliary files the exercise may refer to.


Principle
=========

Data entry routines refer to techniques used to optimize `Spatial data acquisition`_ especially in the context of `Digitizing`_ and data imports.
The idea is to automate as much as possible the production of new geographic information by minimizing the amount of data that a human as to manually declare.

.. attention::

    The more people touch the data during the editing phase, the higher the chance errors and data corruption will occur. In general, it is good policy to restrict data editing as much as possible.

From a technical point of view it is important to understand that these routines **always** have to abide by the constraints imposed by the data provider.
Therefore data entry routines exist on two levels: the provider level, and the interface level :numref:`data_entry_routines`.

.. _data_entry_routines:
.. figure:: _static/images/data_entry_routines/data_entry_routines.png
   :alt: Principle of data entry routines
   :figclass: align-center

   Data routine levels

For this exercise we are going to use the case of a dataset that has to be manually digitized to store the footprint of buildings.
The simplified data model :numref:`data_model` shows how this dataset is structured and how it relates with other datasets.

.. _data_model:
.. figure:: _static/images/data_entry_routines/class_diagram.png
   :alt: Simplified data model
   :figclass: align-center

   Simplified data model for ``building`` dataset


This data model is implemented using a geopackage (.gpkg), but ideally it would be implemented in a concurrent access database like PostgreSQL.
From the data model we can have an overview of the constraints that have to be enforced. We are now going to optimize the data entry through interface optimizations.



Widgets
=======

Before starting to tweak our data entry interface, lets take a look at how it looks and feels by default.

1. **Task** Having the ``topographic_map`` as background map, try to digitize at least one of the buildings footprints into the ``building`` layer.

You will see :numref:`default_menu` that you have to manually enter the information yourself into all the fields and in some cases you simply do not know what value to enter.

.. _default_menu:
.. figure:: _static/images/data_entry_routines/default_menu.png
   :alt: default menu
   :figclass: align-center

   Default data entry interface

Clearly, this is not convenient at all. In order to make the data entry more efficient we will start by defining what type of widgets should be used for each attribute of our table.

.. attention::

   In the context of the ``Vector layer properties`` dialog in QGIS, a widget defines the type of interface the user will see when editing a layer. You can learn more about widgets in the `official documentation <https://docs.qgis.org/testing/en/docs/user_manual/working_with_vector/vector_properties.html#edit-widgets/>`_

2. **Task** From the ``Layers panel``, *right-click* on layer ``building`` an then click on ``Properties``. From the ``Layer properties`` dialog go access the ``Attributes form`` tab :numref:`attributes_form`

.. _attributes_form:
.. figure:: _static/images/data_entry_routines/attributes_form.png
   :alt: attributes form
   :figclass: align-center

   The ``Attributes form`` tab


3. **Task** Define your first widget on field ``fid``. The widget type will be ``Hidden`` :numref:`widget_example`.

.. _widget_example:
.. figure:: _static/images/data_entry_routines/widget_example.png
   :alt: attributes form
   :figclass: align-center

   Widget definition example

4. **Task** Continue defining the widget types field by field according the parameters indicated in :numref:`widgets_building`. In the end hit the ``Apply`` button.

.. _widgets_building:
.. csv-table:: Building widgets
   :file: _static/csv/widgets_building.csv
   :widths: 20,20,20,40
   :header-rows: 1

If you now try to digitize one of the buildings, the interface is different :numref:`after_widget`

.. _after_widget:
.. figure:: _static/images/data_entry_routines/after_widget.png
   :alt: after widget
   :figclass: align-center

   Data entry interface after widget definition

However this is still not good. Some fields are grayed out and cannot be edited. These fields are to be automatically calculated, but for that we need to look into the QGIS expressions

Expressions
===========

QGIS expressions engine offers powerful possibilities when it comes to styling, analyses and, of course, editing data.

.. attention::

    Expressions are a fundamental part of workflows and productivity in QGIS. A full description of all the expressions is available in the `official documentation <https://docs.qgis.org/testing/en/docs/user_manual/working_with_vector/expression.html?highlight=expressions/>`_

In our case we are interested in defining what the default value for a given field is. This default value can be the output of an expression.

5. **Task** Define your first default expression on field ``land_use``. Enter this expression:

   .. code-block::

      aggregate(
      layer:= 'land_use',
      aggregate:='concatenate',
      expression:= LU_DESCRIP,
      concatenator:='',
      filter:=intersects($geometry, geometry(@parent)))


   as the ``Default value`` and make sure the option ``Apply default value on update`` is checked :numref:`expression_example`.

.. _expression_example:
.. figure:: _static/images/data_entry_routines/expression_example.png
   :alt: expression example
   :figclass: align-center

   Expression example

6. **Task** Continue defining the default expressions according to the definitions provided in :numref:`expressions_building`. In the end hit the ``Apply`` button.

.. _expressions_building:
.. csv-table:: Building expressions
   :file: _static/csv/expressions_building.csv
   :widths: 20,60
   :header-rows: 1

I everything went well, if you now proceed to digitize your buildings you should observe that most of the fields are now pre-filled :numref:`after_expressions` making the data entry proccess more reliable and faster.

.. _after_expressions:
.. figure:: _static/images/data_entry_routines/after_expressions.png
   :alt: after expressions
   :figclass: align-center

   Data entry interface after defining default expressions

To make the interface as simple as possible :numref:`minimal_interface`, you can also opt to change the widget type of fields currently not editable to ``Hidden``.
Those fields are ``allowed use``, ``official``, ``registered``, ``street``, ``perimeter_m`` and ``area_m2``.

.. _minimal_interface:
.. figure:: _static/images/data_entry_routines/minimal_interface.png
   :alt: after expressions
   :figclass: align-center

   Data entry interface after hiding autofill fields

workflows
=========

Another type of data entry routine is related with importing from external sources. These sources often take form of a topographic survey where each surveyed point is stored in a table or CSV file.
These points might represent a geographic phenomena representable by a point, in which case each surveyed point will be integrated as geometry of type point in the GIS System.

This integration can get tricky when these points are actually the vertices of a more complex geometry, for example a polygon representing a recently surveyed land parcel like shown in :numref:`t_survey_1`

.. _t_survey_1:
.. csv-table:: Parcel vertices
   :file: _static/csv/t_survey_1.csv
   :widths: 17,17,17,17,17,17
   :header-rows: 1

The workflow required to transform such a table into a geometry is deeply dependent on the overall data model adopted for survey works.
But a relative simple way to do it would be a succession of steps where the output of each of these steps is the input to the next operation until
the final output is obtained.

In the example we will explore, this workflow consists of
``Import the csv as point data`` >
``Generate a line connecting these dots`` >
``Close the line to obtain a polygon`` >
``Fix geometry`` >
``> FINAL OUTPUT``

This succession of steps is tedious and time consuming, especially if it is a recurrent task. A better way to do it is to build a `Model` (or workflow) in QGIS that chains this steps into one single operation :numref:`import_survey_model` that can even be executed as a *batch process* if needed.

.. _import_survey_model:
.. figure:: _static/images/data_entry_routines/import_survey_model.png
   :alt: import survey model
   :figclass: align-center

   Model to import survey data in CSV format

Along with the data for this exercise you have a folder named ``surveys``. Inside you will see 30 CSV files similat to the one shown in :numref:`t_survey_1`, each representing a different topographic survey (i.e. different parcel). We will now use these files to demonstrate how a possible approach to build workflow to import external data.

7. **Task** Import the model ``import_surveys.model3`` into your collection of processing tools :numref:`add_model` you will find this file inside the ``models`` folder.

.. _add_model:
.. figure:: _static/images/data_entry_routines/add_model.png
   :alt: add model
   :figclass: align-center

   Adding a model to the ``Processing toolbox``

8. **Task** From the ``Processing Toolbox``, filter by ``import survey``. *right-click* on it and choose ``Exectute as Batch Process`` :numref:`execute_batch_process`.

.. _execute_batch_process:
.. figure:: _static/images/data_entry_routines/execute_batch_process.png
   :alt: execute batch process
   :figclass: align-center

   Starting a Batch Process

9. **Task** From the ``Processing Toolbox``, filter by ``import survey``. *right-click* on it and choose ``Exectute as Batch Process`` :numref:`execute_batch_process`.


10. **Task** Provide the necessary parameters to execute the batch operation. Check the video below to see how it is done

.. raw:: html

       <iframe width="672" height="378" src="https://www.youtube.com/embed/nVTw18s_knw" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

The end product is a collection of 30 layers with point geometries representing the vertices of the polygons and 30 layers of polygon geometries representing the parcels :numref:`import_final`

.. _import_final:
.. figure:: _static/images/data_entry_routines/import_final.png
   :alt: execute batch process
   :figclass: align-center

   Result of the batch import