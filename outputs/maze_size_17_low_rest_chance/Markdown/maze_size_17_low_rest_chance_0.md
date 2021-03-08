
# Parameters

    Name :                      maze_size_17_low_rest_chance-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     17
    Height :                    17
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14876390675 function calls (14723034152 primitive calls) in 35680.06 seconds

##    Ordered by: cumulative time
   List reduced from 457 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35706.029 35706.029 {built-in method builtins.exec}
                      1    0.924    0.924 35706.029 35706.029 <string>:1(<module>)
                      1  120.566  120.566 35705.105 35705.105 main.py:10(teleport)
                5479800   18.014    0.000 11912.924    0.002 agent.py:26(learn)
                5479800  319.245    0.000 10023.836    0.002 learner.py:42(Qlearn)
                2739900  256.353    0.000 9390.933    0.003 collector.py:36(collect)
               13699500 8013.053    0.001 9103.264    0.001 {built-in method builtins.sum}
                2739900   92.048    0.000 7115.114    0.003 agent.py:50(_learn)
        172457024/19167248  666.657    0.000 5326.100    0.000 module.py:866(_call_impl)
               13687448   38.334    0.000 4942.320    0.000 network.py:24(forward)
                2739900   10.832    0.000 4879.933    0.002 game.py:21(step)
               13687448  172.573    0.000 4818.117    0.000 container.py:117(forward)
                2739900   79.651    0.000 4765.596    0.002 agent.py:101(_learn)
                2739900   12.826    0.000 4254.902    0.002 layers.py:212(step)
                5479800   44.807    0.000 3866.120    0.001 optimizer.py:84(wrapper)
                5479800   23.546    0.000 3667.588    0.001 grad_mode.py:24(decorate_context)
                5479800  144.861    0.000 3593.257    0.001 adam.py:55(step)
                5467748  123.669    0.000 3321.569    0.001 agent.py:45(__call__)
                5479800  752.370    0.000 3276.620    0.001 _functional.py:53(adam)
                2739900  991.230    0.000 2642.921    0.001 agent.py:77(interveen)
                5479800   22.743    0.000 2594.754    0.000 tensor.py:195(backward)
                5479800   21.494    0.000 2571.280    0.000 __init__.py:68(backward)
                5479800 2445.453    0.000 2445.453    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2739900  181.694    0.000 2141.179    0.001 layers.py:17(step)
                2739901  231.739    0.000 2081.875    0.001 layers.py:192(update)
              273990000  184.864    0.000 1931.973    0.000 layer.py:66(move)
                2739900 1124.658    0.000 1924.286    0.001 replaybuffer.py:27(teleporter_save_data)
                2739900  954.005    0.000 1803.066    0.001 replaybuffer.py:23(sample_data)
               27374896   59.518    0.000 1768.804    0.000 conv.py:398(forward)
               27374896   35.509    0.000 1683.709    0.000 conv.py:390(_conv_forward)
               27374896 1648.201    0.000 1648.201    0.000 {built-in method conv2d}
                2739900  903.988    0.000 1595.272    0.001 agent.py:59(modify)
              273990000  117.202    0.000 1421.584    0.000 layers.py:223(isFree)
               35582544   72.743    0.000 1357.074    0.000 linear.py:93(forward)
              388365176 1233.473    0.000 1304.382    0.000 layer.py:63(isFree)
               35582544   30.104    0.000 1252.579    0.000 functional.py:1737(linear)
               35582544 1216.016    0.000 1216.016    0.000 {built-in method torch._C._nn.linear}
               16440492   28.681    0.000 1126.532    0.000 tensor.py:575(__iter__)
               16440492 1073.654    0.000 1073.654    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2739900   38.409    0.000 1051.045    0.000 agent.py:96(__call__)
                8207648   47.995    0.000 1027.608    0.000 agent.py:54(modify_board)
               11580971  934.848    0.000  934.848    0.000 {built-in method tensor}
               21907148  813.311    0.000  813.311    0.000 {built-in method cat}
                5479800    6.271    0.000  780.416    0.000 game.py:17(board)
                 634854    6.861    0.000  730.608    0.001 layers.py:233(restart)
               49269992   41.098    0.000  722.970    0.000 activation.py:713(forward)
               77835780  708.959    0.000  708.959    0.000 {built-in method clone}
                8207648  687.185    0.000  687.185    0.000 {built-in method torch._C._nn.one_hot}
              273990100   71.512    0.000  684.565    0.000 {built-in method builtins.all}
               49269992   41.434    0.000  681.871    0.000 functional.py:1364(leaky_relu)
                2739900   49.829    0.000  662.025    0.000 replaybuffer.py:19(stacker)
              822056513  183.897    0.000  642.813    0.000 layers.py:197(<genexpr>)
               49269992  632.160    0.000  632.160    0.000 {built-in method torch._C._nn.leaky_relu}
               98636400  624.076    0.000  624.076    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 634854    1.452    0.000  599.929    0.001 levels.py:8(__init__)
                5479800  112.265    0.000  599.113    0.000 optimizer.py:189(zero_grad)
                 634854    3.033    0.000  598.477    0.001 level.py:8(__init__)
                 634854  118.359    0.000  588.586    0.001 levels.py:11(generate)
               98636400  565.983    0.000  565.983    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              273990100  290.327    0.000  437.712    0.000 layers.py:65(isDone)
               49318200  384.956    0.000  384.956    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                8219703  149.673    0.000  365.354    0.000 layer.py:90(update)
                5467748  124.370    0.000  339.052    0.000 exploration.py:53(softmaxer)
               49318200  328.540    0.000  328.540    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 634854  164.847    0.000  318.130    0.001 levels.py:76(RFS)
               49318200  308.066    0.000  308.066    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               49318200  300.403    0.000  300.403    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              345227454  220.410    0.000  272.371    0.000 tensor.py:906(grad)
              273990000  192.002    0.000  249.581    0.000 layers.py:229(check)
               49318200  235.618    0.000  235.618    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5479800    7.391    0.000  224.947    0.000 loss.py:527(forward)
                5479800   20.364    0.000  217.556    0.000 functional.py:2898(mse_loss)
                3374754   71.091    0.000  188.426    0.000 random.py:315(sample)
               86043428  161.327    0.000  161.327    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              338836858  157.819    0.000  157.819    0.000 layer.py:85(elements)
                5479800  134.579    0.000  134.579    0.000 {built-in method torch._C._nn.mse_loss}
        819143947/819143945   94.330    0.000  134.363    0.000 {built-in method builtins.len}
             1427686429  128.670    0.000  128.670    0.000 layer.py:59(positions)
                1904562   11.211    0.000  123.024    0.000 layer.py:40(restart)
                5480619  121.986    0.000  121.986    0.000 {built-in method max}
               27374896   17.823    0.000  121.489    0.000 flatten.py:39(forward)
                8219700   10.793    0.000  114.030    0.000 tensor.py:525(__rsub__)
                2739900    9.986    0.000  113.255    0.000 exploration.py:47(epsilonGreedy)
              178973825   74.063    0.000  107.158    0.000 random.py:250(_randbelow_with_getrandbits)
                5467748  105.163    0.000  105.163    0.000 {built-in method multinomial}
               27374896  103.667    0.000  103.667    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              188897516  103.456    0.000  103.456    0.000 {built-in method torch._C._get_tracing_state}
                8219700  101.416    0.000  101.416    0.000 {built-in method rsub}
                5479800   20.876    0.000   99.463    0.000 __init__.py:28(_make_grads)
              352711999   66.765    0.000   96.218    0.000 enum.py:646(__hash__)
                5479800   94.293    0.000   94.293    0.000 {built-in method gather}
               10959600   21.649    0.000   94.141    0.000 profiler.py:615(__enter__)
               10959600   14.004    0.000   81.684    0.000 profiler.py:607(__init__)
                 634954   47.199    0.000   81.603    0.000 layers.py:37(reset)
              139615728   80.570    0.000   80.578    0.000 module.py:934(__getattr__)
                2739901   79.786    0.000   79.786    0.000 {built-in method nonzero}
              161310044   58.268    0.000   77.828    0.000 layer.py:76(add)
              159983208   49.123    0.000   74.705    0.000 levels.py:33(<genexpr>)
                5479800   74.388    0.000   74.388    0.000 {built-in method ones_like}
               10959600   72.492    0.000   72.492    0.000 {built-in method torch._ops.profiler._record_function_enter}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9393247: <maze_size_17_low_rest_chance_0> in cluster <dcc> Done

Job <maze_size_17_low_rest_chance_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Mar  8 02:11:20 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Mar  8 02:11:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 02:11:21 2021
Terminated at Mon Mar  8 12:06:43 2021
Results reported at Mon Mar  8 12:06:43 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35622.60 sec.
    Max Memory :                                 6206 MB
    Average Memory :                             4381.75 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1986.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35765 sec.
    Turnaround time :                            35723 sec.

The output (if any) is above this job summary.

