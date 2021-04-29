
# Parameters

    Name :                      Causal3_Conver1-2
    Main :                      CFagent
    Level :                     Levels.Causal3
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
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
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                1
    Counterfacts :              1
    Topn :                      3
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      66129119056 function calls (65790883025 primitive calls) in 86116.73 seconds

##    Ordered by: cumulative time
   List reduced from 508 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86116.727 86116.727 {built-in method builtins.exec}
                      1    4.415    4.415 86116.726 86116.726 <string>:1(<module>)
                      1  388.689  388.689 86112.312 86112.312 main.py:79(CFagent)
               10429047   41.715    0.000 26223.243    0.003 agent.py:29(learn)
               10429046  663.411    0.000 21319.876    0.002 learner.py:42(Qlearn)
                3476349   15.533    0.000 18865.242    0.005 game.py:41(step)
                3476349   20.510    0.000 18119.489    0.005 layers.py:718(step)
        378008364/39774024 1570.146    0.000 12669.647    0.000 module.py:866(_call_impl)
               29344978   85.419    0.000 11869.268    0.000 network.py:27(forward)
               29344978  383.214    0.000 11590.462    0.000 container.py:117(forward)
                3476349  307.992    0.000 10724.046    0.003 layers.py:17(step)
              347626313  595.164    0.000 10384.349    0.000 layer.py:98(move)
                3476349 1230.924    0.000 10301.170    0.003 agent.py:212(counterfact)
                3476349  380.516    0.000 10192.890    0.003 agent.py:54(_learn)
                3476349  377.793    0.000 9358.639    0.003 agent.py:204(_learn)
               10429046   92.330    0.000 8347.635    0.001 optimizer.py:84(wrapper)
               10429046   46.919    0.000 7938.152    0.001 grad_mode.py:24(decorate_context)
               10429046  326.271    0.000 7789.100    0.001 adam.py:55(step)
                3476350  531.669    0.000 7345.516    0.002 layers.py:684(update)
               10429046 1626.639    0.000 7087.061    0.001 _functional.py:53(adam)
                3476349  107.011    0.000 6607.131    0.002 agent.py:117(_learn)
                9456579  252.385    0.000 6245.105    0.001 agent.py:49(__call__)
              347626313 1282.244    0.000 6209.438    0.000 layers.py:735(check)
                3476349 4979.336    0.001 6092.064    0.002 replaybuffer.py:22(sample_data)
                3476349 3427.622    0.001 6085.926    0.002 replaybuffer.py:28(teleporter_save_data)
                3476349 4798.276    0.001 5866.055    0.002 replaybuffer.py:67(sample_data)
               10429046   44.390    0.000 5498.173    0.001 tensor.py:195(backward)
               10429046   44.333    0.000 5452.240    0.001 __init__.py:68(backward)
                3476349 2959.110    0.001 5239.763    0.002 agent.py:88(interveen)
               10429046 5195.452    0.000 5195.452    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               51358768 4457.101    0.000 4457.101    0.000 {built-in method tensor}
               43371355   30.420    0.000 4259.738    0.000 game.py:37(board)
               58689956  137.910    0.000 4244.677    0.000 conv.py:398(forward)
               58689956   82.213    0.000 4042.980    0.000 conv.py:390(_conv_forward)
               58689956 3960.766    0.000 3960.766    0.000 {built-in method conv2d}
               55621592 2153.028    0.000 3745.867    0.000 layer.py:167(NoRock_update)
                2506656   52.030    0.000 3311.598    0.001 agent.py:176(choose_action)
               81082236  172.334    0.000 3289.428    0.000 linear.py:93(forward)
               81082236   69.067    0.000 3029.542    0.000 functional.py:1737(linear)
              347626313  549.054    0.000 3019.327    0.000 layers.py:729(isFree)
               81082236 2943.568    0.000 2943.568    0.000 {built-in method torch._C._nn.linear}
                3476349 1801.080    0.001 2686.108    0.001 agent.py:67(modify)
              254298923 2579.863    0.000 2579.863    0.000 {built-in method clone}
             2491500658 2046.081    0.000 2470.273    0.000 layer.py:95(isFree)
                6101212   67.202    0.000 2030.658    0.000 layers.py:740(restart)
               47696413 1838.892    0.000 1838.892    0.000 {built-in method cat}
                3476349 1344.418    0.000 1775.311    0.001 replaybuffer.py:73(CF_save_data)
              110427214   93.969    0.000 1743.173    0.000 activation.py:713(forward)
               12932928   82.310    0.000 1718.520    0.000 agent.py:59(modify_board)
              110427214   97.793    0.000 1649.204    0.000 functional.py:1364(leaky_relu)
                3476348   59.555    0.000 1611.635    0.000 agent.py:172(__call__)
             5547210664 1051.506    0.000 1562.303    0.000 enum.py:646(__hash__)
              110427214 1532.832    0.000 1532.832    0.000 {built-in method torch._C._nn.leaky_relu}
                3476349   56.190    0.000 1510.947    0.000 agent.py:112(__call__)
                6101212   32.115    0.000 1438.413    0.000 level.py:8(__init__)
              194675524 1386.326    0.000 1386.326    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              345010138  325.183    0.000 1357.072    0.000 {built-in method builtins.any}
              347635000  174.710    0.000 1341.742    0.000 {built-in method builtins.all}
              347626313  823.152    0.000 1309.234    0.000 layers.py:286(check)
               10429046  221.221    0.000 1246.243    0.000 optimizer.py:189(zero_grad)
              194675524 1226.724    0.000 1226.724    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             1759451229  489.664    0.000 1214.030    0.000 layers.py:690(<genexpr>)
              347626313  702.946    0.000 1185.810    0.000 layers.py:246(check)
                6101212  130.826    0.000 1144.428    0.000 levels.py:164(generate)
               12932928 1126.932    0.000 1126.932    0.000 {built-in method torch._C._nn.one_hot}
             3073804092  844.437    0.000 1031.889    0.000 layers.py:700(<genexpr>)
             1393161470  904.563    0.000  904.563    0.000 layer.py:146(elements)
                3476349   65.685    0.000  848.161    0.000 replaybuffer.py:18(stacker)
               12202424  118.888    0.000  836.948    0.000 level.py:41(notUsed)
               97337762  819.371    0.000  819.371    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3476348   65.204    0.000  810.855    0.000 replaybuffer.py:63(stacker)
               97337762  706.803    0.000  706.803    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             6766806019  657.940    0.000  657.940    0.000 layer.py:91(positions)
               97337762  650.713    0.000  650.713    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              347626313  410.429    0.000  648.420    0.000 layers.py:313(check)
        7924261552/7924261549  577.011    0.000  647.314    0.000 {built-in method builtins.len}
              347635000  428.652    0.000  646.287    0.000 layers.py:113(isDone)
               97337762  643.479    0.000  643.479    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               19155122  240.157    0.000  630.786    0.000 random.py:315(sample)
                9456579  233.980    0.000  622.591    0.000 exploration.py:53(softmaxer)
              347626313  380.900    0.000  597.098    0.000 layers.py:273(check)
              681364418  471.707    0.000  590.797    0.000 tensor.py:906(grad)
              270708199  569.028    0.000  569.028    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3476349  321.949    0.000  548.456    0.000 collector.py:46(collect)
             5547250231  510.804    0.000  510.804    0.000 {built-in method builtins.hash}
               48809696   62.019    0.000  506.851    0.000 layer.py:69(restart)
              347626313  330.238    0.000  496.285    0.000 layers.py:48(check)
               97337762  490.885    0.000  490.885    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2506656  482.411    0.000  482.411    0.000 agent.py:187(convert_values)
               10429046   16.337    0.000  460.088    0.000 loss.py:527(forward)
               10429046   41.607    0.000  443.751    0.000 functional.py:2898(mse_loss)
              339764292  296.751    0.000  394.854    0.000 layer.py:126(remove)
              347626313  267.337    0.000  393.903    0.000 layers.py:23(check)
              643799309  267.672    0.000  369.821    0.000 layer.py:130(add)
               12202424   13.918    0.000  339.115    0.000 level.py:38(elementsIn)
                6101312  164.390    0.000  324.652    0.000 layers.py:36(reset)
              468217850  220.529    0.000  322.103    0.000 random.py:250(_randbelow_with_getrandbits)
               58689956   42.496    0.000  288.747    0.000 flatten.py:39(forward)
              400268640  283.344    0.000  283.344    0.000 level.py:32(inverse)
               10429046  273.735    0.000  273.735    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9579156: <Causal3_Conver1_2> in cluster <dcc> Done

Job <Causal3_Conver1_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Apr 27 02:44:05 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Apr 27 05:40:21 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 27 05:40:21 2021
Terminated at Wed Apr 28 05:35:48 2021
Results reported at Wed Apr 28 05:35:48 2021

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

    CPU time :                                   85904.58 sec.
    Max Memory :                                 9808 MB
    Average Memory :                             6545.19 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               6576.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86128 sec.
    Turnaround time :                            96703 sec.

The output (if any) is above this job summary.

