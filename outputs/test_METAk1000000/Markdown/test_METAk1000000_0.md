
# Parameters

    Name :                      test_METAk1000000-0
    Main :                      metateleport
    Level :                     Levels.Causal1
    Hours :                     4.0
    Batch :                     100
    Width :                     9
    Height :                    9
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
    Layer rock :                False
    Layer dirt :                False
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         1000000.0
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      5211771141 function calls (5152484802 primitive calls) in 14116.36 seconds

##    Ordered by: cumulative time
   List reduced from 463 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14116.358 14116.358 {built-in method builtins.exec}
                      1    5.472    5.472 14116.358 14116.358 <string>:1(<module>)
                      1   65.166   65.166 14110.886 14110.886 main.py:14(metateleport)
                1972965    8.929    0.000 5079.084    0.003 agent.py:27(learn)
                1972965  128.277    0.000 4065.295    0.002 learner.py:42(Qlearn)
                1315310 3490.076    0.003 4014.095    0.003 replaybuffer.py:23(sample_data)
                1315310   50.611    0.000 3804.313    0.003 agent.py:51(_learn)
        66417210/7132570  290.300    0.000 2261.180    0.000 module.py:866(_call_impl)
                5159605   14.986    0.000 2100.957    0.000 network.py:24(forward)
                5159605   72.724    0.000 2049.138    0.000 container.py:117(forward)
                2528985   73.513    0.000 1697.644    0.001 agent.py:46(__call__)
                1972965   18.985    0.000 1558.149    0.001 optimizer.py:84(wrapper)
                1972965   10.927    0.000 1477.401    0.001 grad_mode.py:24(decorate_context)
                1972965   66.807    0.000 1443.193    0.001 adam.py:55(step)
                 657655    3.599    0.000 1420.866    0.002 game.py:27(step)
                 657655    4.492    0.000 1309.675    0.002 layers.py:475(step)
                1972965  301.039    0.000 1304.512    0.001 _functional.py:53(adam)
                 657655   21.413    0.000 1261.294    0.002 agent.py:110(_learn)
                1315310  393.778    0.000 1179.210    0.001 agent.py:81(interveen)
                1972965    8.722    0.000 1064.237    0.001 tensor.py:195(backward)
                1972965    9.503    0.000 1055.234    0.001 __init__.py:68(backward)
                1972965 1004.036    0.001 1004.036    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 657655  612.275    0.001  942.481    0.001 agent.py:114(metamodify)
                1315310  503.114    0.000  853.283    0.001 replaybuffer.py:27(teleporter_save_data)
               10319210   24.984    0.000  752.883    0.000 conv.py:398(forward)
               10319210   15.786    0.000  715.036    0.000 conv.py:390(_conv_forward)
               10319210  699.250    0.000  699.250    0.000 {built-in method conv2d}
                 657655   65.427    0.000  665.866    0.001 layers.py:18(step)
                 657656   71.839    0.000  631.560    0.001 layers.py:446(update)
               65765500   78.053    0.000  593.451    0.000 layer.py:76(move)
               14163505   31.376    0.000  576.036    0.000 linear.py:93(forward)
               14163505   11.945    0.000  527.456    0.000 functional.py:1737(linear)
               14163505  512.695    0.000  512.695    0.000 {built-in method torch._C._nn.linear}
                3844295   35.524    0.000  506.442    0.000 agent.py:55(modify_board)
               11736155  471.000    0.000  471.000    0.000 {built-in method cat}
                1315310   41.017    0.000  415.164    0.000 replaybuffer.py:19(stacker)
               65765500   48.841    0.000  355.256    0.000 layers.py:486(isFree)
                3844295  325.692    0.000  325.692    0.000 {built-in method torch._C._nn.one_hot}
                 657655   13.225    0.000  314.223    0.000 agent.py:105(__call__)
               31774354  312.195    0.000  312.195    0.000 {built-in method clone}
              187614124  275.467    0.000  306.415    0.000 layer.py:73(isFree)
               19323110   17.005    0.000  299.761    0.000 activation.py:713(forward)
               19323110   17.034    0.000  282.756    0.000 functional.py:1364(leaky_relu)
               19323110  262.518    0.000  262.518    0.000 {built-in method torch._C._nn.leaky_relu}
               36828680  250.361    0.000  250.361    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                1972965   41.685    0.000  229.864    0.000 optimizer.py:189(zero_grad)
               36828680  224.182    0.000  224.182    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                1972968  124.684    0.000  206.369    0.000 layer.py:137(NoRock_update)
                3733296  198.381    0.000  198.381    0.000 {built-in method tensor}
               65765600   19.099    0.000  190.018    0.000 {built-in method builtins.all}
              197730856   47.812    0.000  178.678    0.000 layers.py:452(<genexpr>)
                2528985   61.950    0.000  168.372    0.000 exploration.py:53(softmaxer)
               18414340  150.737    0.000  150.737    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1972965    2.676    0.000  147.911    0.000 game.py:23(board)
                 657655   80.006    0.000  136.170    0.000 collector.py:54(collect)
                 575372    5.368    0.000  135.827    0.000 layers.py:496(restart)
               18414340  131.901    0.000  131.901    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               65765600   87.043    0.000  125.163    0.000 layers.py:110(isDone)
               18414340  120.424    0.000  120.424    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               18414340  120.363    0.000  120.363    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              128900464   90.800    0.000  111.457    0.000 tensor.py:906(grad)
                1315310   42.326    0.000  106.263    0.000 random.py:315(sample)
                1972965    4.020    0.000   96.101    0.000 loss.py:527(forward)
                1972965   10.020    0.000   92.081    0.000 functional.py:2898(mse_loss)
                 575372    3.084    0.000   91.608    0.000 level.py:8(__init__)
               18414340   88.468    0.000   88.468    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 575372    5.469    0.000   76.008    0.000 levels.py:122(generate)
               34960994   74.296    0.000   74.296    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               65765500   53.894    0.000   69.119    0.000 layers.py:492(check)
                 657655    4.252    0.000   67.480    0.000 exploration.py:47(epsilonGreedy)
                1726116   15.982    0.000   65.609    0.000 level.py:41(notUsed)
        500183868/500183865   49.010    0.000   64.994    0.000 {built-in method builtins.len}
                5918895   63.976    0.000   63.976    0.000 {built-in method sum}
                1972965   54.841    0.000   54.841    0.000 {built-in method torch._C._nn.mse_loss}
                2528985   53.614    0.000   53.614    0.000 {built-in method multinomial}
              164361763   52.787    0.000   52.787    0.000 layer.py:116(elements)
               80490160   37.942    0.000   52.732    0.000 layer.py:100(add)
                3288275    6.277    0.000   52.522    0.000 tensor.py:525(__rsub__)
               10319210    8.245    0.000   50.111    0.000 flatten.py:39(forward)
                1973282   49.319    0.000   49.319    0.000 {built-in method max}
               60924312   32.952    0.000   48.528    0.000 layer.py:96(remove)
                3288275   45.454    0.000   45.454    0.000 {built-in method rsub}
               67511216   30.147    0.000   44.576    0.000 random.py:250(_randbelow_with_getrandbits)
                1315312   42.105    0.000   42.105    0.000 {built-in method nonzero}
               10319210   41.866    0.000   41.866    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               54130304   41.075    0.000   41.079    0.000 module.py:934(__getattr__)
                1972965    9.238    0.000   39.623    0.000 __init__.py:28(_make_grads)
               67733024   39.017    0.000   39.017    0.000 {built-in method torch._C._get_tracing_state}
                 441381   18.660    0.000   38.857    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
                1972965   38.622    0.000   38.622    0.000 {built-in method gather}
                3945930    9.599    0.000   38.184    0.000 profiler.py:615(__enter__)
                1726116    2.573    0.000   38.043    0.000 layer.py:50(restart)
              389893328   36.439    0.000   36.439    0.000 layer.py:69(positions)
                3072003   35.079    0.000   35.079    0.000 {method 'long' of 'torch._C._TensorBase' objects}
              115247595   23.112    0.000   33.320    0.000 enum.py:646(__hash__)
                4603589   32.863    0.000   32.863    0.000 {built-in method zeros}
                2529237    3.062    0.000   32.761    0.000 functional.py:1553(softmax)
                 575472   15.641    0.000   31.439    0.000 layers.py:33(reset)
                3945930    6.117    0.000   31.057    0.000 profiler.py:607(__init__)
                2529237   29.320    0.000   29.320    0.000 {method 'softmax' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9457746: <test_METAk1000000_0> in cluster <dcc> Done

Job <test_METAk1000000_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 17:24:29 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 17:24:31 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 17:24:31 2021
Terminated at Wed Mar 24 21:19:59 2021
Results reported at Wed Mar 24 21:19:59 2021

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

    CPU time :                                   14077.57 sec.
    Max Memory :                                 4885 MB
    Average Memory :                             4263.07 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               3307.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14145 sec.
    Turnaround time :                            14130 sec.

The output (if any) is above this job summary.

