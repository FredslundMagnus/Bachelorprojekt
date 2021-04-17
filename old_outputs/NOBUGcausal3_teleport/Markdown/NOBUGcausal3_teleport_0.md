
# Parameters

    Name :                      NOBUGcausal3_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal3
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                0
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      45277623002 function calls (45063631151 primitive calls) in 57317.59 seconds

##    Ordered by: cumulative time
   List reduced from 475 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57317.590 57317.590 {built-in method builtins.exec}
                      1    1.931    1.931 57317.590 57317.590 <string>:1(<module>)
                      1  177.492  177.492 57315.659 57315.659 main.py:42(teleport)
                7647432   25.567    0.000 21812.941    0.003 agent.py:28(learn)
                7647432  569.756    0.000 18441.812    0.002 learner.py:42(Qlearn)
                3823716   16.058    0.000 13911.385    0.004 game.py:36(step)
                3823716  405.468    0.000 13160.783    0.003 agent.py:53(_learn)
                3823716   21.675    0.000 13052.185    0.003 layers.py:594(step)
        240745414/26754574  955.285    0.000 8760.387    0.000 module.py:866(_call_impl)
                3823716  289.413    0.000 8659.848    0.002 layers.py:18(step)
                3823716  112.868    0.000 8611.237    0.002 agent.py:114(_learn)
              382371600  437.866    0.000 8338.259    0.000 layer.py:82(move)
               19107142   54.584    0.000 8165.451    0.000 network.py:24(forward)
               19107142  251.754    0.000 7991.449    0.000 container.py:117(forward)
                7647432   67.211    0.000 7708.843    0.001 optimizer.py:84(wrapper)
                7647432   33.022    0.000 7396.903    0.001 grad_mode.py:24(decorate_context)
                7647432  211.081    0.000 7291.672    0.001 adam.py:55(step)
                7647432 1503.546    0.000 6841.510    0.001 _functional.py:53(adam)
                3823716 3195.518    0.001 5862.450    0.002 replaybuffer.py:28(teleporter_save_data)
                7635994  192.218    0.000 5451.443    0.001 agent.py:48(__call__)
                3823716 2519.898    0.001 5179.572    0.001 agent.py:85(interveen)
              382371600  849.856    0.000 4888.364    0.000 layers.py:611(check)
                7647432   32.262    0.000 4656.253    0.001 tensor.py:195(backward)
                7647432   30.920    0.000 4622.875    0.001 __init__.py:68(backward)
                3823716 3186.807    0.001 4542.299    0.001 replaybuffer.py:22(sample_data)
                7647432 4421.659    0.001 4421.659    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3823717  388.276    0.000 4343.125    0.001 layers.py:565(update)
               38214284   85.063    0.000 2938.027    0.000 conv.py:398(forward)
                3823716 1714.469    0.000 2869.956    0.001 agent.py:66(modify)
               38214284   51.105    0.000 2816.342    0.000 conv.py:390(_conv_forward)
               38214284 2765.238    0.000 2765.238    0.000 {built-in method conv2d}
              382371600  498.024    0.000 2617.400    0.000 layers.py:605(isFree)
               49673994  100.658    0.000 2275.027    0.000 linear.py:93(forward)
              181115868 2209.168    0.000 2209.168    0.000 {built-in method clone}
               49673994   41.961    0.000 2126.915    0.000 functional.py:1737(linear)
             2565500528 1751.937    0.000 2119.376    0.000 layer.py:79(isFree)
               49673994 2074.889    0.000 2074.889    0.000 {built-in method torch._C._nn.linear}
               30589736 1013.025    0.000 1808.423    0.000 layer.py:143(NoRock_update)
                3823716   56.492    0.000 1729.744    0.000 agent.py:109(__call__)
               11459710   83.220    0.000 1645.888    0.000 agent.py:58(modify_board)
              137653776 1387.693    0.000 1387.693    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               34402006 1362.005    0.000 1362.005    0.000 {built-in method cat}
               68781136   64.830    0.000 1290.217    0.000 activation.py:713(forward)
              137653776 1229.235    0.000 1229.235    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               68781136   55.997    0.000 1225.387    0.000 functional.py:1364(leaky_relu)
               16393647 1211.281    0.000 1211.281    0.000 {built-in method tensor}
             5069307020  840.048    0.000 1205.763    0.000 enum.py:646(__hash__)
              382371600  730.291    0.000 1170.439    0.000 layers.py:303(check)
               68781136 1157.627    0.000 1157.627    0.000 {built-in method torch._C._nn.leaky_relu}
                3823716   72.544    0.000 1091.818    0.000 replaybuffer.py:18(stacker)
                7647432  178.428    0.000 1079.175    0.000 optimizer.py:189(zero_grad)
              382371600  650.306    0.000 1076.435    0.000 layers.py:262(check)
                3811480   37.731    0.000 1067.630    0.000 layers.py:615(restart)
               11459710 1049.970    0.000 1049.970    0.000 {built-in method torch._C._nn.one_hot}
                7647432    9.681    0.000  943.405    0.000 game.py:32(board)
              382371700  100.880    0.000  936.270    0.000 {built-in method builtins.all}
             1162175445  255.605    0.000  877.612    0.000 layers.py:571(<genexpr>)
                3823716  462.131    0.000  763.852    0.000 collector.py:54(collect)
               68826888  761.057    0.000  761.057    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3811480   18.253    0.000  733.717    0.000 level.py:8(__init__)
               68826888  671.366    0.000  671.366    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               68826888  636.579    0.000  636.579    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               68826888  631.710    0.000  631.710    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              382371600  403.298    0.000  630.013    0.000 layers.py:329(check)
              382371700  395.302    0.000  590.891    0.000 layers.py:111(isDone)
              192575578  587.271    0.000  587.271    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              382371600  372.296    0.000  582.395    0.000 layers.py:288(check)
                7635994  211.305    0.000  571.641    0.000 exploration.py:53(softmaxer)
                3811480   74.486    0.000  567.423    0.000 levels.py:164(generate)
             6579368302  559.011    0.000  559.011    0.000 layer.py:75(positions)
             1115454189  494.012    0.000  494.012    0.000 layer.py:122(elements)
              382371600  325.443    0.000  489.113    0.000 layers.py:47(check)
               68826888  489.052    0.000  489.052    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                7622960   61.063    0.000  393.491    0.000 level.py:41(notUsed)
              481788270  317.639    0.000  393.224    0.000 tensor.py:906(grad)
                7647432   11.014    0.000  368.692    0.000 loss.py:527(forward)
             5069334923  365.720    0.000  365.720    0.000 {built-in method builtins.hash}
                7647432   28.325    0.000  357.678    0.000 functional.py:2898(mse_loss)
               11446676  122.739    0.000  327.163    0.000 random.py:315(sample)
               22942296  320.180    0.000  320.180    0.000 {built-in method sum}
        3609537281/3609537279  262.395    0.000  316.753    0.000 {built-in method builtins.len}
               30491840   36.827    0.000  286.446    0.000 layer.py:56(restart)
              528288259  207.303    0.000  285.139    0.000 layer.py:106(add)
              333436480  155.629    0.000  235.797    0.000 layer.py:102(remove)
                7647432  235.251    0.000  235.251    0.000 {built-in method torch._C._nn.mse_loss}
               38214284   25.629    0.000  216.143    0.000 flatten.py:39(forward)
               11471148   16.916    0.000  215.417    0.000 tensor.py:525(__rsub__)
                7648577  213.930    0.000  213.930    0.000 {built-in method max}
                3823716   17.431    0.000  210.983    0.000 exploration.py:47(epsilonGreedy)
               11471148  195.660    0.000  195.660    0.000 {built-in method rsub}
               38214284  190.514    0.000  190.514    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
             1935080677  183.813    0.000  183.813    0.000 layer.py:183(isBlocking)
                7635994  183.034    0.000  183.034    0.000 {built-in method multinomial}
                3811580   90.503    0.000  181.724    0.000 layers.py:33(reset)
              283445732  120.662    0.000  176.476    0.000 random.py:250(_randbelow_with_getrandbits)
              244570656  167.463    0.000  167.463    0.000 {built-in method torch._C._get_tracing_state}
                7647432   30.976    0.000  163.649    0.000 __init__.py:28(_make_grads)
                7647432  163.414    0.000  163.414    0.000 {built-in method gather}
               15294864   34.480    0.000  162.041    0.000 profiler.py:615(__enter__)
              250047605  159.238    0.000  159.238    0.000 level.py:32(inverse)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9494236: <NOBUGcausal3_teleport_0> in cluster <dcc> Done

Job <NOBUGcausal3_teleport_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:52 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:26 2021
Results reported at Sun Apr  4 18:55:26 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   57163.81 sec.
    Max Memory :                                 7837 MB
    Average Memory :                             5375.50 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8547.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57372 sec.
    Turnaround time :                            57334 sec.

The output (if any) is above this job summary.

