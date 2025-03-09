.. _api.diffract:

==================
Diffractometer
==================

.. index:: !design; diffractometer

Diffractometers are built as a subclass of
:class:`~hklpy2.diffract.DiffractometerBase()`, adding a variety of
positioners as ophyd Components.  In an instance of that subclass, user
sets :attr:`~hklpy2.diffract.DiffractometerBase.backend_solver` by calling
:func:`~hklpy2.misc.solver_factory`.  In this call, the user specifies the solver,
the geometry, and defines which Components (of the diffractometer) are to be used as
pseudos and reals.  The backend implements
:meth:`~hklpy2.backends.base.SolverBase.forward`,
:meth:`~hklpy2.backends.base.SolverBase.inverse`, and all related support, for
only the pseudos and reals that are identified.

.. grid:: 2

    .. grid-item-card:: :material-outlined:`check_box;3em` A |solver| is not needed to:

      - define subclass of :class:`~hklpy2.diffract.DiffractometerBase()` and create instance
      - create instance of :class:`~hklpy2.blocks.sample.Sample()`
      - create instance of :class:`~hklpy2.blocks.lattice.Lattice()`
      - create instance of :class:`~hklpy2.wavelength_support.WavelengthBase()` subclass
      - create instance of :class:`~hklpy2.backends.base.SolverBase()` subclass
      - set :attr:`~hklpy2.wavelength_support.WavelengthBase.wavelength`
      - list *available* solvers: (:func:`~hklpy2.misc.solvers`)
      - review saved orientation details

    .. grid-item-card:: :material-outlined:`rule;3em` A |solver| is needed to:

      - list available |solver| :attr:`~hklpy2.backends.base.SolverBase.geometries`
      - list a |solver| geometry's required
        :attr:`~hklpy2.backends.base.SolverBase.pseudo_axis_names`,
        :attr:`~hklpy2.backends.base.SolverBase.real_axis_names`,
        :attr:`~hklpy2.backends.base.SolverBase.extra_axis_names`,
        :attr:`~hklpy2.backends.base.SolverBase.modes`
      - create instance of :class:`~hklpy2.blocks.reflection.Reflection()`
      - define or compute a :math:`UB` matrix
        (:meth:`~hklpy2.backends.base.SolverBase.calculateOrientation`)
      - :meth:`~hklpy2.backends.base.SolverBase.forward`
        and :meth:`~hklpy2.backends.base.SolverBase.inverse`
      - determine the diffractometer :attr:`~hklpy2.diffract.DiffractometerBase.position`
      - save or restore orientation details
      - refine lattice parameters

The :class:`~hklpy2.diffract.DiffractometerBase()` class should
be a thin interface. Most real diffractometer capability should be
provided in the :class:`~hklpy2.ops.Operations()` class (or one of
its attributes, such as :attr:`~hklpy2.ops.Operations.solver`
and :attr:`~hklpy2.ops.Operations.sample`)

.. rubric:: Operations-related methods and properties
.. autosummary::

    ~hklpy2.diffract.DiffractometerBase.auto_assign_axes (method)
    ~hklpy2.diffract.DiffractometerBase.forward (method)
    ~hklpy2.diffract.DiffractometerBase.inverse (method)
    ~hklpy2.diffract.DiffractometerBase.position (method)
    ~hklpy2.diffract.DiffractometerBase.pseudo_axis_names (property)
    ~hklpy2.diffract.DiffractometerBase.real_axis_names (property)
    ~hklpy2.diffract.DiffractometerBase.wh (method)

.. rubric:: Sample-related methods and properties
.. autosummary::

    ~hklpy2.diffract.DiffractometerBase.add_reflection (method)
    ~hklpy2.diffract.DiffractometerBase.add_sample (method)
    ~hklpy2.diffract.DiffractometerBase.sample (property)
    ~hklpy2.diffract.DiffractometerBase.samples (property)

.. rubric:: Solver-related methods and properties
.. autosummary::

    ~hklpy2.diffract.DiffractometerBase.geometry (ophyd Signal)
    ~hklpy2.diffract.DiffractometerBase.solver (property)
    ~hklpy2.diffract.DiffractometerBase.solver_name (ophyd Signal)

.. rubric:: Related methods and properties from other classes
.. autosummary::

    ~hklpy2.ops.Operations.assign_axes (method)
    ~hklpy2.backends.base.SolverBase.extra_axis_names (property)
    ~hklpy2.blocks.sample.Sample.lattice (property)
    ~hklpy2.blocks.sample.Sample.refine_lattice (method)
    ~hklpy2.blocks.sample.Sample.reflections (property)
    ~hklpy2.ops.Operations.set_solver (method)
    ~hklpy2.blocks.sample.Sample.U (property)
    ~hklpy2.blocks.sample.Sample.UB (property)
