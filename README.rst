test-markov
================================================================================

Via https://docs.pymc.io/en/v3/about.html#purpose

PyMC3 is a probabilistic programming package for Python that allows users to fit Bayesian models using a variety of numerical methods, most notably Markov chain Monte Carlo (MCMC) and variational inference (VI). Its flexibility and extensibility make it applicable to a large suite of problems. Along with core model specification and fitting functionality, PyMC3 includes functionality for summarizing output and for model diagnostics.

Via https://towardsdatascience.com/introduction-to-linear-regression-in-python-c12a072bedf0

Linear regression is a basic predictive analytics technique that uses historical data to predict an output variable. It is popular for predictive modelling because it is easily understood and can be explained using plain English.

::

    % time make demo                                                                                    22-04-19 - 10:30:18
    python demo.py
    ['230.1', '37.8', '69.2', '22.1']
    /Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/deprecat/classic.py:215: FutureWarning: In v4.0, pm.sample will return an `arviz.InferenceData` object instead of a `MultiTrace` by default. You can pass return_inferencedata=True or return_inferencedata=False to be safe and silence this warning.
      return wrapped_(*args_, **kwargs_)
    Auto-assigning NUTS sampler...
    Initializing NUTS using jitter+adapt_diag...
    Multiprocess sampling (4 chains in 4 jobs)
    NUTS: [noise, weights]
    ['230.1', '37.8', '69.2', '22.1']
    /Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/deprecat/classic.py:215: FutureWarning: In v4.0, pm.sample will return an `arviz.InferenceData` object instead of a `MultiTrace` by default. You can pass return_inferencedata=True or return_inferencedata=False to be safe and silence this warning.
      return wrapped_(*args_, **kwargs_)
    Auto-assigning NUTS sampler...
    Initializing NUTS using jitter+adapt_diag...
    Multiprocess sampling (4 chains in 4 jobs)
    NUTS: [noise, weights]
    Traceback (most recent call last):
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/forkserver.py", line 274, in main
        code = _serve_one(child_r, fds,
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/forkserver.py", line 313, in _serve_one
        code = spawn._main(child_r, parent_sentinel)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/spawn.py", line 125, in _main
        prepare(preparation_data)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/spawn.py", line 236, in prepare
        _fixup_main_from_path(data['init_main_from_path'])
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/spawn.py", line 287, in _fixup_main_from_path
        main_content = runpy.run_path(main_path,
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/runpy.py", line 269, in run_path
        return _run_module_code(code, init_globals, run_name,
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/runpy.py", line 96, in _run_module_code
        _run_code(code, mod_globals, init_globals,
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/runpy.py", line 86, in _run_code
        exec(code, run_globals)
      File "/Users/alexclark/Developer/test-markov/demo.py", line 38, in <module>
        posterior = pm.sample()
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/deprecat/classic.py", line 215, in wrapper_function
        return wrapped_(*args_, **kwargs_)
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/sampling.py", line 575, in sample
        trace = _mp_sample(**sample_args, **parallel_args)
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/sampling.py", line 1480, in _mp_sample
        sampler = ps.ParallelSampler(
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 431, in __init__
        self._samplers = [
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 432, in <listcomp>
        ProcessAdapter(
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 292, in __init__
        self._process.start()
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/process.py", line 121, in start
        self._popen = self._Popen(self)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/context.py", line 291, in _Popen
        return Popen(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_forkserver.py", line 35, in __init__
        super().__init__(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_fork.py", line 19, in __init__
        self._launch(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_forkserver.py", line 42, in _launch
        prep_data = spawn.get_preparation_data(process_obj._name)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/spawn.py", line 154, in get_preparation_data
        _check_not_importing_main()
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/spawn.py", line 134, in _check_not_importing_main
        raise RuntimeError('''
    RuntimeError: 
            An attempt has been made to start a new process before the
            current process has finished its bootstrapping phase.

            This probably means that you are not using fork to start your
            child processes and you have forgotten to use the proper idiom
            in the main module:

                if __name__ == '__main__':
                    freeze_support()
                    ...

            The "freeze_support()" line can be omitted if the program
            is not going to be frozen to produce an executable.
    Traceback (most recent call last):
      File "/Users/alexclark/Developer/test-markov/demo.py", line 38, in <module>
        posterior = pm.sample()
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/deprecat/classic.py", line 215, in wrapper_function
        return wrapped_(*args_, **kwargs_)
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/sampling.py", line 575, in sample
        trace = _mp_sample(**sample_args, **parallel_args)
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/sampling.py", line 1480, in _mp_sample
        sampler = ps.ParallelSampler(
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 431, in __init__
        self._samplers = [
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 432, in <listcomp>
        ProcessAdapter(
      File "/Users/alexclark/Developer/test-markov/lib/python3.10/site-packages/pymc3/parallel_sampling.py", line 292, in __init__
        self._process.start()
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/process.py", line 121, in start
        self._popen = self._Popen(self)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/context.py", line 291, in _Popen
        return Popen(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_forkserver.py", line 35, in __init__
        super().__init__(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_fork.py", line 19, in __init__
        self._launch(process_obj)
      File "/usr/local/Cellar/python@3.10/3.10.2/Frameworks/Python.framework/Versions/3.10/lib/python3.10/multiprocessing/popen_forkserver.py", line 58, in _launch
        f.write(buf.getbuffer())
    BrokenPipeError: [Errno 32] Broken pipe
    make: *** [demo] Error 1
    make demo  6.88s user 0.97s system 58% cpu 13.374 total
    (test-markov) 

