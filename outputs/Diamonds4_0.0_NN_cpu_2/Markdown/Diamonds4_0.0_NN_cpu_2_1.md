/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu_2-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     1
    Model explore :             100000
    Samples :                   5
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       1
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      13480288602 function calls (13252307419 primitive calls) in 35700.28 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.278 35700.278 {built-in method builtins.exec}
                      1    0.001    0.001 35700.278 35700.278 <string>:1(<module>)
                      1   65.468   65.468 35700.277 35700.277 allGraphsTrain.py:13(graphTrain)
        241929383/27395693 1348.877    0.000 12948.242    0.000 module.py:715(_call_impl)
               21453369  403.354    0.000 12307.713    0.001 container.py:115(forward)
                5640632   70.157    0.000 10707.649    0.002 BayesianNN.py:57(learn)
                 301692   65.057    0.000 10645.088    0.035 allGraphsTrain.py:40(<listcomp>)
                4478271   20.464    0.000 10539.975    0.002 allGraphs.py:179(getInterventionsmodel)
                5640632   90.224    0.000 10149.182    0.002 BayesianNN.py:21(learn)
               20849985   78.985    0.000 9898.515    0.000 BayesianNN.py:18(forward)
                 301692 1828.694    0.006 9773.677    0.032 allGraphs.py:156(transformNot)
        17330797/4324284  881.482    0.000 8844.694    0.002 allGraphs.py:186(recursiveBEST)
               15209353  207.312    0.000 8633.280    0.001 BayesianNN.py:61(predict)
                 301692    1.613    0.000 4515.357    0.015 agent.py:29(learn)
                 301692   25.548    0.000 4512.975    0.015 agent.py:117(_learn)
                 301692   23.948    0.000 4487.427    0.015 learner.py:42(Qlearn)
                5942324   43.679    0.000 4440.871    0.001 grad_mode.py:23(decorate_context)
                5942324  198.877    0.000 4316.120    0.001 adam.py:55(step)
                5942324   43.350    0.000 4136.281    0.001 tensor.py:181(backward)
                5942324   26.210    0.000 4092.931    0.001 __init__.py:68(backward)
                 301692   20.073    0.000 3972.287    0.013 allGraphs.py:141(transform)
                5942324 3951.341    0.001 3951.341    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               62549955   85.138    0.000 3426.938    0.000 dropout.py:57(forward)
               63756723  217.980    0.000 3392.398    0.000 linear.py:92(forward)
               62549955  335.365    0.000 3341.800    0.000 functional.py:960(dropout)
                5942324  849.520    0.000 3291.758    0.001 functional.py:53(adam)
               63756723  357.213    0.000 3086.136    0.000 functional.py:1669(linear)
               62549955 2934.619    0.000 2934.619    0.000 {built-in method dropout}
                 603384    2.445    0.000 2710.337    0.004 network.py:28(forward)
                1206768    4.466    0.000 2272.751    0.002 conv.py:422(forward)
                1206768    4.346    0.000 2266.808    0.002 conv.py:414(_conv_forward)
                1206768 2261.837    0.002 2261.837    0.002 {built-in method conv2d}
                 301692    1.573    0.000 2015.663    0.007 game.py:42(step)
                 301692    2.386    0.000 1981.614    0.007 layers.py:827(step)
                 301692   19.824    0.000 1892.388    0.006 allGraphsTrain.py:33(<listcomp>)
               30470993  920.879    0.000 1872.571    0.000 allGraphs.py:114(states)
               20849985 1250.737    0.000 1730.349    0.000 BayesianNN.py:43(convert_data)
               63756723 1617.576    0.000 1617.576    0.000 {built-in method addmm}
              271523200 1555.337    0.000 1555.337    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              253801356  900.197    0.000 1467.884    0.000 tensor.py:933(grad)
          594555/153987   43.060    0.000 1388.998    0.009 allGraphs.py:202(recursiveExplore)
                 301692    5.142    0.000 1354.325    0.004 agent.py:112(__call__)
               64360107   73.015    0.000 1095.838    0.000 activation.py:713(forward)
                5942324  127.036    0.000 1082.729    0.000 optimizer.py:167(zero_grad)
                 301692   34.531    0.000 1053.126    0.003 layers.py:17(step)
               64360107  121.772    0.000 1022.823    0.000 functional.py:1292(leaky_relu)
               30169200   72.933    0.000 1014.866    0.000 layer.py:106(move)
              390273140  306.979    0.000  960.093    0.000 overrides.py:1070(has_torch_function)
                 301693   63.450    0.000  923.231    0.003 layers.py:793(update)
               64360107  888.950    0.000  888.950    0.000 {built-in method torch._C._nn.leaky_relu}
               45426433  178.667    0.000  799.800    0.000 tensor.py:21(wrapped)
               72514656  783.677    0.000  783.677    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              495480974  293.590    0.000  779.350    0.000 {built-in method builtins.any}
               63756723  722.179    0.000  722.179    0.000 {method 't' of 'torch._C._TensorBase' objects}
               30169200  141.182    0.000  636.628    0.000 layers.py:844(check)
              307335440  547.012    0.000  547.012    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               72514656  501.594    0.000  501.594    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 301692   37.744    0.000  481.825    0.002 allGraphsTrain.py:51(<listcomp>)
                 301692   52.675    0.000  422.553    0.001 allGraphsTrain.py:44(<listcomp>)
                5942324   12.100    0.000  395.844    0.000 loss.py:445(forward)
                5942324   43.845    0.000  383.744    0.000 functional.py:2637(mse_loss)
                 602837    8.866    0.000  379.685    0.001 layers.py:849(restart)
              880760626  301.148    0.000  367.333    0.000 overrides.py:1083(<genexpr>)
               41699971  361.654    0.000  361.654    0.000 {built-in method zeros}
                7286206  349.143    0.000  349.143    0.000 {built-in method tensor}
               36257328  337.998    0.000  337.998    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               13748773   69.109    0.000  325.988    0.000 tensor.py:506(__rsub__)
                5986732    8.541    0.000  320.328    0.000 game.py:38(board)
               36257328  317.069    0.000  317.069    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 602837    4.175    0.000  308.348    0.001 level.py:8(__init__)
                4478271   42.736    0.000  283.922    0.000 allGraphs.py:167(format)
              242834459  272.338    0.000  272.338    0.000 {built-in method torch._C._get_tracing_state}
               31677660  271.597    0.000  271.597    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 602837   10.936    0.000  269.961    0.000 levels.py:456(generate)
               36257328  265.480    0.000  265.480    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               13748773  256.880    0.000  256.880    0.000 {built-in method rsub}
                2894166   43.610    0.000  248.201    0.000 level.py:41(notUsed)
              647827539  167.626    0.000  246.878    0.000 enum.py:646(__hash__)
               30169200   64.136    0.000  240.714    0.000 layers.py:838(isFree)
                 301692   95.171    0.000  237.327    0.001 agent.py:67(modify)
                5942324  228.284    0.000  228.284    0.000 {built-in method torch._C._nn.mse_loss}
               36257328  223.519    0.000  223.519    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2111851  118.285    0.000  206.266    0.000 layer.py:175(NoRock_update)
               30169200  201.185    0.000  201.185    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               52225953  183.458    0.000  183.458    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               28276829  181.266    0.000  181.266    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              199787615  138.960    0.000  176.578    0.000 layer.py:103(isFree)
               75595733   41.605    0.000  170.433    0.000 {built-in method builtins.all}
               13447081  169.062    0.000  169.062    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 905076    4.963    0.000  156.735    0.000 tensor.py:576(__iter__)
                 905076  148.841    0.000  148.841    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               36257438   66.583    0.000  147.401    0.000 tensor.py:596(__hash__)
        889459529/889459527  135.311    0.000  142.845    0.000 {built-in method builtins.len}
              157021928  137.149    0.000  137.150    0.000 module.py:765(__getattr__)
              989170901  135.133    0.000  135.133    0.000 {method 'values' of 'collections.OrderedDict' objects}
               30169200   79.133    0.000  126.996    0.000 layers.py:632(check)
                2894166    3.349    0.000  120.955    0.000 level.py:38(elementsIn)
               30169200   73.959    0.000  119.755    0.000 layers.py:602(check)
               30169200   73.370    0.000  117.957    0.000 layers.py:617(check)
              236531704   93.309    0.000  112.945    0.000 layers.py:809(<genexpr>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668411: <Diamonds4_0.0_NN_cpu_2_1> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_2_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:59:02 2021
Job was executed on host(s) <n-62-21-105>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:03 2021
Terminated at Thu May 20 08:54:08 2021
Results reported at Thu May 20 08:54:08 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35701.02 sec.
    Max Memory :                                 109 MB
    Average Memory :                             102.93 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16275.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35756 sec.
    Turnaround time :                            35706 sec.

The output (if any) is above this job summary.

