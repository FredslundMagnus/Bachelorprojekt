/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds2_0.5_NN_cpu_2-2
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.5
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
    Num :                       2
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      16444281407 function calls (16123546394 primitive calls) in 35700.18 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.182 35700.182 {built-in method builtins.exec}
                      1    0.002    0.002 35700.181 35700.181 <string>:1(<module>)
                      1   95.901   95.901 35700.179 35700.179 allGraphsTrain.py:13(graphTrain)
        337802817/37103857 1262.578    0.000 11712.872    0.000 module.py:715(_call_impl)
               30069896  350.006    0.000 11122.617    0.000 container.py:115(forward)
                 321570 2303.559    0.007 11112.621    0.035 allGraphs.py:156(transformNot)
                 321570   69.028    0.000 10957.170    0.034 allGraphsTrain.py:40(<listcomp>)
                5082481   20.055    0.000 10842.075    0.002 allGraphs.py:179(getInterventionsmodel)
                6712391   66.358    0.000 9645.189    0.001 BayesianNN.py:57(learn)
        24274635/4908675  978.437    0.000 9054.872    0.002 allGraphs.py:186(recursiveBEST)
                6712391   78.569    0.000 9018.415    0.001 BayesianNN.py:21(learn)
               29426756   71.097    0.000 8982.131    0.000 BayesianNN.py:18(forward)
               22714365  224.055    0.000 8801.611    0.000 BayesianNN.py:61(predict)
                7033961   41.014    0.000 4125.911    0.001 grad_mode.py:23(decorate_context)
                 321570    2.304    0.000 4103.220    0.013 agent.py:29(learn)
                 321570   52.607    0.000 4100.122    0.013 agent.py:117(_learn)
                 321570   26.724    0.000 4047.515    0.013 learner.py:42(Qlearn)
                7033961  201.409    0.000 4005.963    0.001 adam.py:55(step)
                7033961   36.184    0.000 3796.170    0.001 tensor.py:181(backward)
                7033961   26.475    0.000 3759.986    0.001 __init__.py:68(backward)
                7033961 3631.145    0.001 3631.145    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               89566548  198.446    0.000 3124.954    0.000 linear.py:92(forward)
               88280268   76.044    0.000 3042.483    0.000 dropout.py:57(forward)
                7033961  756.360    0.000 3008.411    0.000 functional.py:53(adam)
               88280268  297.479    0.000 2966.438    0.000 functional.py:960(dropout)
               89566548  333.892    0.000 2840.844    0.000 functional.py:1669(linear)
               88280268 2586.158    0.000 2586.158    0.000 {built-in method dropout}
                 321570   58.221    0.000 2554.284    0.008 allGraphsTrain.py:33(<listcomp>)
               32478671 1200.014    0.000 2496.070    0.000 allGraphs.py:114(states)
                 643140    2.479    0.000 2447.283    0.004 network.py:28(forward)
                 321570   22.453    0.000 2371.156    0.007 allGraphs.py:141(transform)
               29426756 1774.009    0.000 2293.688    0.000 BayesianNN.py:43(convert_data)
              418041600 2043.186    0.000 2043.186    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                1286280    4.847    0.000 1960.951    0.002 conv.py:422(forward)
                1286280    6.023    0.000 1954.178    0.002 conv.py:414(_conv_forward)
                1286280 1947.487    0.002 1947.487    0.002 {built-in method conv2d}
                 321570    2.310    0.000 1820.325    0.006 game.py:42(step)
                 321570    3.070    0.000 1776.535    0.006 layers.py:827(step)
               89566548 1477.504    0.000 1477.504    0.000 {built-in method addmm}
          843487/173806   49.458    0.000 1447.321    0.008 allGraphs.py:202(recursiveExplore)
              299928402  836.910    0.000 1397.239    0.000 tensor.py:933(grad)
                 321570    7.220    0.000 1320.528    0.004 agent.py:112(__call__)
               90209688   73.164    0.000 1048.147    0.000 activation.py:713(forward)
                7033961  121.092    0.000 1029.942    0.000 optimizer.py:167(zero_grad)
               90209688  109.341    0.000  974.983    0.000 functional.py:1292(leaky_relu)
                 321570   38.874    0.000  955.157    0.003 layers.py:17(step)
              471510867  303.569    0.000  946.005    0.000 overrides.py:1070(has_torch_function)
               32157000   68.056    0.000  912.696    0.000 layer.py:106(move)
               90209688  853.498    0.000  853.498    0.000 {built-in method torch._C._nn.leaky_relu}
                 321571   59.593    0.000  814.110    0.003 layers.py:793(update)
              606942395  294.418    0.000  780.651    0.000 {built-in method builtins.any}
               85693812  751.370    0.000  751.370    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              456913559  705.173    0.000  705.173    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               54122061  151.833    0.000  699.516    0.000 tensor.py:21(wrapped)
               89566548  629.193    0.000  629.193    0.000 {method 't' of 'torch._C._TensorBase' objects}
               85693812  473.357    0.000  473.357    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               32157000  114.734    0.000  462.293    0.000 layers.py:844(check)
                8073330  409.844    0.000  409.844    0.000 {built-in method tensor}
                 321570   27.088    0.000  388.731    0.001 allGraphsTrain.py:51(<listcomp>)
                 321570   50.653    0.000  382.042    0.001 allGraphsTrain.py:44(<listcomp>)
                6690332    7.772    0.000  378.198    0.000 game.py:38(board)
             1071757183  295.393    0.000  360.503    0.000 overrides.py:1083(<genexpr>)
               58853513  359.073    0.000  359.073    0.000 {built-in method zeros}
                7033961   11.816    0.000  346.234    0.000 loss.py:445(forward)
                7033961   44.277    0.000  334.418    0.000 functional.py:2637(mse_loss)
               20357211   68.517    0.000  319.337    0.000 tensor.py:506(__rsub__)
                5082481   43.402    0.000  317.406    0.000 allGraphs.py:167(format)
               32157000   71.211    0.000  313.259    0.000 layers.py:838(isFree)
               42846906  292.285    0.000  292.285    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               42846906  287.383    0.000  287.383    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               20357211  250.820    0.000  250.820    0.000 {built-in method rsub}
                 360042    5.830    0.000  244.664    0.001 layers.py:849(restart)
              281960001  199.568    0.000  242.048    0.000 layer.py:103(isFree)
               42846906  233.389    0.000  233.389    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2894139  125.783    0.000  225.532    0.000 layer.py:175(NoRock_update)
              338767527  225.518    0.000  225.518    0.000 {built-in method torch._C._get_tracing_state}
                 321570   77.421    0.000  223.984    0.001 agent.py:67(modify)
               33764850  218.442    0.000  218.442    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 360042    2.923    0.000  203.767    0.001 level.py:8(__init__)
               42846906  199.517    0.000  199.517    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              570226119  134.875    0.000  196.865    0.000 enum.py:646(__hash__)
                7033961  187.478    0.000  187.478    0.000 {built-in method torch._C._nn.mse_loss}
               38443219  182.982    0.000  182.982    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               32157000  180.835    0.000  180.835    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 360042    7.482    0.000  180.457    0.001 levels.py:249(generate)
               62870036  173.915    0.000  173.915    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 964710    5.386    0.000  171.687    0.000 tensor.py:576(__iter__)
               86279161   46.722    0.000  170.847    0.000 {built-in method builtins.all}
               20035641  168.581    0.000  168.581    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                2340257   28.611    0.000  165.405    0.000 level.py:41(notUsed)
                 964710  163.143    0.000  163.143    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              198603582  110.799    0.000  146.165    0.000 types.py:171(__get__)
               42847016   63.358    0.000  143.861    0.000 tensor.py:596(__hash__)
             1381281164  140.763    0.000  140.763    0.000 {method 'values' of 'collections.OrderedDict' objects}
              218488932  138.367    0.000  138.368    0.000 module.py:765(__getattr__)
        1176846448/1176846446  126.447    0.000  132.299    0.000 {built-in method builtins.len}
              317970580   98.866    0.000  120.446    0.000 layers.py:809(<genexpr>)
               42846906  108.533    0.000  108.533    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               30713036   24.018    0.000  102.010    0.000 flatten.py:39(forward)
                3321864   98.600    0.000   98.600    0.000 {built-in method cat}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668394: <Diamonds2_0.5_NN_cpu_2_2> in cluster <dcc> Done

Job <Diamonds2_0.5_NN_cpu_2_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:58:59 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:59:01 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:59:01 2021
Terminated at Thu May 20 08:54:03 2021
Results reported at Thu May 20 08:54:03 2021

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

    CPU time :                                   35616.10 sec.
    Max Memory :                                 105 MB
    Average Memory :                             98.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16279.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35772 sec.
    Turnaround time :                            35704 sec.

The output (if any) is above this job summary.

