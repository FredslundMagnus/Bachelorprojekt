/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     3
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


      11863818066 function calls (11384477388 primitive calls) in 35700.94 seconds

##    Ordered by: cumulative time
   List reduced from 443 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.939 35700.939 {built-in method builtins.exec}
                      1    0.001    0.001 35700.939 35700.939 <string>:1(<module>)
                      1   39.222   39.222 35700.937 35700.937 allGraphsTrain.py:13(graphTrain)
                 126366   26.706    0.000 25742.989    0.204 allGraphsTrain.py:40(<listcomp>)
                 936953    5.869    0.000 25706.085    0.027 allGraphs.py:179(getInterventionsmodel)
        40678104/781374 2233.272    0.000 24186.073    0.031 allGraphs.py:186(recursiveBEST)
        484614404/45605504 2606.142    0.000 21757.933    0.000 module.py:715(_call_impl)
               43900890  821.054    0.000 21259.445    0.000 container.py:115(forward)
               43648158  149.682    0.000 20441.806    0.000 BayesianNN.py:18(forward)
               37626640 1213.715    0.000 18823.349    0.001 BayesianNN.py:65(predict_no_convert)
              130944474  186.556    0.000 7069.293    0.000 dropout.py:57(forward)
              130944474  668.960    0.000 6882.736    0.000 functional.py:960(dropout)
              131449938  430.516    0.000 6745.192    0.000 linear.py:92(forward)
              131449938  702.247    0.000 6148.875    0.000 functional.py:1669(linear)
              130944474 6062.526    0.000 6062.526    0.000 {built-in method dropout}
                 126366  822.923    0.007 3366.389    0.027 allGraphs.py:156(transformNot)
                1578248   22.380    0.000 3232.890    0.002 BayesianNN.py:57(learn)
              131449938 3212.853    0.000 3212.853    0.000 {built-in method addmm}
                1578248   26.769    0.000 3062.900    0.002 BayesianNN.py:21(learn)
                4443270   65.083    0.000 2627.177    0.001 BayesianNN.py:61(predict)
                 126366    1.010    0.000 2212.082    0.018 agent.py:29(learn)
                 126366   18.341    0.000 2210.596    0.017 agent.py:117(_learn)
                 126366   13.270    0.000 2192.255    0.017 learner.py:42(Qlearn)
              131702670  147.914    0.000 2023.707    0.000 activation.py:713(forward)
              131702670  224.255    0.000 1875.793    0.000 functional.py:1292(leaky_relu)
                1704614   13.817    0.000 1700.927    0.001 tensor.py:181(backward)
                1704614    9.407    0.000 1687.110    0.001 __init__.py:68(backward)
                1704614 1640.688    0.001 1640.688    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              131702670 1626.922    0.000 1626.922    0.000 {built-in method torch._C._nn.leaky_relu}
              131449938 1444.365    0.000 1444.365    0.000 {method 't' of 'torch._C._TensorBase' objects}
                1704614   14.227    0.000 1425.014    0.001 grad_mode.py:23(decorate_context)
          590215/155579   48.767    0.000 1424.806    0.009 allGraphs.py:202(recursiveExplore)
                 252732    1.328    0.000 1388.869    0.005 network.py:28(forward)
                1704614   63.238    0.000 1383.379    0.001 adam.py:55(step)
                 126366    8.439    0.000 1242.710    0.010 allGraphs.py:141(transform)
                 505464    2.737    0.000 1173.627    0.002 conv.py:422(forward)
                 505464    2.710    0.000 1170.113    0.002 conv.py:414(_conv_forward)
                 505464 1167.120    0.002 1167.120    0.002 {built-in method conv2d}
                1704614  276.458    0.000 1083.389    0.001 functional.py:53(adam)
               53726162  251.118    0.000 1029.436    0.000 tensor.py:21(wrapped)
               40457732  193.786    0.000  980.430    0.000 tensor.py:506(__rsub__)
                 126366   28.670    0.000  883.045    0.007 allGraphsTrain.py:33(<listcomp>)
               12763067  408.869    0.000  854.386    0.000 allGraphs.py:114(states)
                 126366    0.974    0.000  852.910    0.007 game.py:42(step)
                 126366    1.495    0.000  831.733    0.007 layers.py:827(step)
               40457732  786.644    0.000  786.644    0.000 {built-in method rsub}
              239709161  242.136    0.000  778.726    0.000 overrides.py:1070(has_torch_function)
              113729800  726.890    0.000  726.890    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 126366    3.122    0.000  702.904    0.006 agent.py:112(__call__)
              387014014  260.314    0.000  616.776    0.000 {built-in method builtins.any}
                6021518  388.473    0.000  545.980    0.000 BayesianNN.py:43(convert_data)
              484993502  534.968    0.000  534.968    0.000 {built-in method torch._C._get_tracing_state}
               40331366  474.175    0.000  474.175    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
                 126366   17.387    0.000  467.948    0.004 layers.py:17(step)
               12636600   31.607    0.000  448.988    0.000 layer.py:106(move)
               73362972  261.192    0.000  424.299    0.000 tensor.py:933(grad)
                 126367   28.400    0.000  360.322    0.003 layers.py:793(update)
                1704614   37.327    0.000  320.010    0.000 optimizer.py:167(zero_grad)
              635283985  252.801    0.000  307.775    0.000 overrides.py:1083(<genexpr>)
             1982358506  270.151    0.000  270.151    0.000 {method 'values' of 'collections.OrderedDict' objects}
               12636600   56.913    0.000  269.836    0.000 layers.py:844(check)
               20960832  263.732    0.000  263.732    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              309390491  244.265    0.000  244.266    0.000 module.py:765(__getattr__)
              127945656  244.064    0.000  244.064    0.000 {method 'item' of 'torch._C._TensorBase' objects}
        1232165109/1232165107  207.913    0.000  211.306    0.000 {built-in method builtins.len}
                 126366   15.008    0.000  198.025    0.002 allGraphsTrain.py:51(<listcomp>)
               56790222  180.385    0.000  180.385    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                 126366   23.216    0.000  178.554    0.001 allGraphsTrain.py:44(<listcomp>)
               44153622   36.247    0.000  171.780    0.000 flatten.py:39(forward)
               20960832  158.637    0.000  158.637    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               66362862   54.067    0.000  144.250    0.000 {built-in method builtins.all}
                2131718  138.867    0.000  138.867    0.000 {built-in method tensor}
                1704614    4.136    0.000  128.772    0.000 loss.py:445(forward)
              132649088   87.496    0.000  127.558    0.000 _VF.py:25(__getattr__)
                1704614   14.542    0.000  124.636    0.000 functional.py:2637(mse_loss)
                 191013    3.117    0.000  123.580    0.001 layers.py:849(restart)
                1568784    2.870    0.000  122.767    0.000 game.py:38(board)
               12043037  121.526    0.000  121.526    0.000 {built-in method zeros}
               12636600   29.294    0.000  118.320    0.000 layers.py:838(isFree)
               10480416  114.743    0.000  114.743    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 126366   42.503    0.000  114.404    0.001 agent.py:67(modify)
               13268430  113.617    0.000  113.617    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              131449938  109.971    0.000  109.971    0.000 functional.py:1686(<listcomp>)
               10480416  101.819    0.000  101.819    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 191013    1.531    0.000   99.525    0.001 level.py:8(__init__)
              372473428   95.202    0.000   95.202    0.000 {built-in method builtins.getattr}
              251585281   65.680    0.000   94.648    0.000 enum.py:646(__hash__)
                 884569   52.593    0.000   92.635    0.000 layer.py:175(NoRock_update)
               42322642   92.186    0.000   92.186    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
               10480416   91.078    0.000   91.078    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               85122152   73.582    0.000   89.026    0.000 layer.py:103(isFree)
                 936953   15.830    0.000   88.623    0.000 allGraphs.py:167(format)
                 191013    3.672    0.000   86.240    0.000 levels.py:456(generate)
               12636600   84.443    0.000   84.443    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
               68739829   63.327    0.000   80.008    0.000 types.py:171(__get__)
                 916314   14.454    0.000   79.016    0.000 level.py:41(notUsed)
                 379098    2.497    0.000   78.665    0.000 tensor.py:576(__iter__)
                 379098   74.457    0.000   74.457    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1704614   73.647    0.000   73.647    0.000 {built-in method torch._C._nn.mse_loss}
               10480416   72.567    0.000   72.567    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9653103: <Diamonds4_0.0_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_1> was submitted from host <n-62-30-5> by user <s183905> in cluster <dcc> at Wed May 19 11:40:33 2021
Job was executed on host(s) <n-62-21-106>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 11:40:35 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 11:40:35 2021
Terminated at Wed May 19 21:35:41 2021
Results reported at Wed May 19 21:35:41 2021

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

    CPU time :                                   35702.81 sec.
    Max Memory :                                 104 MB
    Average Memory :                             99.40 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16280.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35769 sec.
    Turnaround time :                            35708 sec.

The output (if any) is above this job summary.

/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0

# Parameters

    Name :                      Diamonds4_0.0_NN_cpu-1
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


      17644666701 function calls (17342291625 primitive calls) in 35700.23 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35700.232 35700.232 {built-in method builtins.exec}
                      1    0.002    0.002 35700.232 35700.232 <string>:1(<module>)
                      1   87.998   87.998 35700.230 35700.230 allGraphsTrain.py:13(graphTrain)
        319850152/36139822 1229.946    0.000 11841.520    0.000 module.py:715(_call_impl)
               28371033  330.244    0.000 11212.605    0.000 container.py:115(forward)
                7382031   72.594    0.000 10439.831    0.001 BayesianNN.py:57(learn)
                7382031   84.014    0.000 9882.770    0.001 BayesianNN.py:21(learn)
                 386758 1992.461    0.005 9696.517    0.025 allGraphs.py:156(transformNot)
                 386758   76.296    0.000 9591.865    0.025 allGraphsTrain.py:40(<listcomp>)
                5958186   21.520    0.000 9471.848    0.002 allGraphs.py:179(getInterventionsmodel)
               27597517   65.718    0.000 8500.676    0.000 BayesianNN.py:18(forward)
        24100343/5823797  926.766    0.000 8334.545    0.001 allGraphs.py:186(recursiveBEST)
               20215486  201.188    0.000 7565.592    0.000 BayesianNN.py:61(predict)
                 386758    2.778    0.000 4679.553    0.012 agent.py:29(learn)
                 386758  174.217    0.000 4675.817    0.012 agent.py:117(_learn)
                7768789   46.337    0.000 4572.937    0.001 grad_mode.py:23(decorate_context)
                 386758   31.919    0.000 4501.600    0.012 learner.py:42(Qlearn)
                7768789  224.565    0.000 4436.709    0.001 adam.py:55(step)
                 386758   27.441    0.000 4089.225    0.011 allGraphs.py:141(transform)
                7768789   38.427    0.000 3999.256    0.001 tensor.py:181(backward)
                7768789   26.861    0.000 3960.828    0.001 __init__.py:68(backward)
                7768789 3819.524    0.000 3819.524    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7768789  851.598    0.000 3350.560    0.000 functional.py:53(adam)
                 773516    2.964    0.000 3007.577    0.004 network.py:28(forward)
               84339583  185.376    0.000 3001.888    0.000 linear.py:92(forward)
               82792551   71.664    0.000 2870.397    0.000 dropout.py:57(forward)
               82792551  279.433    0.000 2798.734    0.000 functional.py:960(dropout)
               84339583  318.472    0.000 2735.188    0.000 functional.py:1669(linear)
                1547032    5.856    0.000 2524.857    0.002 conv.py:422(forward)
                1547032    6.972    0.000 2516.922    0.002 conv.py:414(_conv_forward)
                1547032 2509.162    0.002 2509.162    0.002 {built-in method conv2d}
               82792551 2441.948    0.000 2441.948    0.000 {built-in method dropout}
                 386758    2.731    0.000 2333.388    0.006 game.py:42(step)
                 386758    3.333    0.000 2285.966    0.006 layers.py:827(step)
                 386758   16.067    0.000 2010.450    0.005 allGraphsTrain.py:33(<listcomp>)
               39062659  966.395    0.000 1994.391    0.000 allGraphs.py:114(states)
               27597517 1235.190    0.000 1692.057    0.000 BayesianNN.py:43(convert_data)
              348082600 1691.149    0.000 1691.149    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 386758    8.462    0.000 1586.347    0.004 agent.py:112(__call__)
              331703810  898.201    0.000 1517.818    0.000 tensor.py:933(grad)
               84339583 1435.275    0.000 1435.275    0.000 {built-in method addmm}
                 386758   47.098    0.000 1258.503    0.003 layers.py:17(step)
               38675800   83.796    0.000 1207.101    0.000 layer.py:106(move)
                7768789  135.087    0.000 1131.849    0.000 optimizer.py:167(zero_grad)
                 386759   69.828    0.000 1019.062    0.003 layers.py:793(update)
              510384287  324.517    0.000 1012.472    0.000 overrides.py:1070(has_torch_function)
               85113099   65.455    0.000  951.597    0.000 activation.py:713(forward)
               85113099  107.245    0.000  886.142    0.000 functional.py:1292(leaky_relu)
               94772500  835.492    0.000  835.492    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              648122694  312.764    0.000  817.006    0.000 {built-in method builtins.any}
          522177/134389   28.550    0.000  808.984    0.006 allGraphs.py:202(recursiveExplore)
               59660682  171.183    0.000  798.038    0.000 tensor.py:21(wrapped)
               85113099  768.141    0.000  768.141    0.000 {built-in method torch._C._nn.leaky_relu}
               38675800  152.227    0.000  718.061    0.000 layers.py:844(check)
              394143519  616.705    0.000  616.705    0.000 {method 'item' of 'torch._C._TensorBase' objects}
               84339583  602.872    0.000  602.872    0.000 {method 't' of 'torch._C._TensorBase' objects}
               94772500  528.162    0.000  528.162    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 386758   33.483    0.000  484.394    0.001 allGraphsTrain.py:51(<listcomp>)
                 386758   60.222    0.000  463.830    0.001 allGraphsTrain.py:44(<listcomp>)
                 814654    9.729    0.000  424.570    0.001 layers.py:849(restart)
                9549198  400.500    0.000  400.500    0.000 {built-in method tensor}
             1152062691  316.137    0.000  384.715    0.000 overrides.py:1083(<genexpr>)
                7768789   11.798    0.000  383.009    0.000 loss.py:445(forward)
                7768789   45.067    0.000  371.211    0.000 functional.py:2637(mse_loss)
                7891977    8.442    0.000  364.944    0.000 game.py:38(board)
                 814654    5.225    0.000  343.623    0.000 level.py:8(__init__)
               55195035  341.096    0.000  341.096    0.000 {built-in method zeros}
               38675800   66.370    0.000  323.637    0.000 layers.py:838(isFree)
               47386250  321.370    0.000  321.370    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               47386250  316.107    0.000  316.107    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                5958186   44.561    0.000  304.167    0.000 allGraphs.py:167(format)
               19051092   63.065    0.000  301.098    0.000 tensor.py:506(__rsub__)
                 814654   12.191    0.000  296.693    0.000 levels.py:456(generate)
               40609590  274.203    0.000  274.203    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3909858   48.277    0.000  271.961    0.000 level.py:41(notUsed)
              812933079  182.809    0.000  264.669    0.000 enum.py:646(__hash__)
                 386758   97.932    0.000  263.815    0.001 agent.py:67(modify)
               47386250  260.244    0.000  260.244    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              255272806  216.794    0.000  257.267    0.000 layer.py:103(isFree)
               19051092  238.033    0.000  238.033    0.000 {built-in method rsub}
                2707313  131.359    0.000  228.909    0.000 layer.py:175(NoRock_update)
               47386250  222.251    0.000  222.251    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               38675800  218.033    0.000  218.033    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              321010426  214.982    0.000  214.982    0.000 {built-in method torch._C._get_tracing_state}
                7768789  212.230    0.000  212.230    0.000 {built-in method torch._C._nn.mse_loss}
                1160274    6.259    0.000  201.588    0.000 tensor.py:576(__iter__)
               67820349  196.504    0.000  196.504    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1160274  191.642    0.000  191.642    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               98336582   50.844    0.000  189.659    0.000 {built-in method builtins.all}
               36915398  176.927    0.000  176.927    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               18664334  167.036    0.000  167.036    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
               47386360   69.247    0.000  157.529    0.000 tensor.py:596(__hash__)
               38675800   92.538    0.000  146.395    0.000 layers.py:602(check)
               38675800   84.434    0.000  135.824    0.000 layers.py:617(check)
              207527415  135.620    0.000  135.621    0.000 module.py:765(__getattr__)
               38675800   84.650    0.000  135.535    0.000 layers.py:632(check)
                3909858    3.936    0.000  133.570    0.000 level.py:38(elementsIn)
        1165191400/1165191398  126.599    0.000  133.553    0.000 {built-in method builtins.len}
             1307771641  131.046    0.000  131.046    0.000 {method 'values' of 'collections.OrderedDict' objects}
               47386250  121.234    0.000  121.234    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9668385: <Diamonds4_0.0_NN_cpu_1> in cluster <dcc> Done

Job <Diamonds4_0.0_NN_cpu_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Wed May 19 22:55:28 2021
Job was executed on host(s) <n-62-11-62>, in queue <hpc>, as user <s183905> in cluster <dcc> at Wed May 19 22:55:30 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed May 19 22:55:30 2021
Terminated at Thu May 20 08:50:35 2021
Results reported at Thu May 20 08:50:35 2021

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

    CPU time :                                   35614.96 sec.
    Max Memory :                                 102 MB
    Average Memory :                             94.77 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16282.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   35734 sec.
    Turnaround time :                            35707 sec.

The output (if any) is above this job summary.

