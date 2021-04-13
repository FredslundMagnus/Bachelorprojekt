
# Parameters

    Name :                      CFv2TESTCAU4cf2-0
    Main :                      CFagentv2
    Level :                     Levels.Causal4
    Failed actions chance :     0.0
    Hours :                     16.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        500000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000
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
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Minutes used :              955 minutes.
    Hours used :                15 hours.

# Profiling


      42699064336 function calls (42530507942 primitive calls) in 57310.39 seconds

##    Ordered by: cumulative time
   List reduced from 528 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57310.389 57310.389 {built-in method builtins.exec}
                      1    5.673    5.673 57310.389 57310.389 <string>:1(<module>)
                      1  162.431  162.431 57304.717 57304.717 main.py:103(CFagentv2)
                5866254   24.135    0.000 14672.403    0.003 agent.py:29(learn)
                1955418   10.131    0.000 13256.949    0.007 game.py:41(step)
                1955418   11.955    0.000 12794.480    0.007 layers.py:719(step)
                5863502  377.675    0.000 11929.889    0.002 learner.py:42(Qlearn)
                1955418  189.326    0.000 7875.273    0.004 layers.py:17(step)
              194243016  577.377    0.000 7667.624    0.000 layer.py:98(move)
                1955418 1475.909    0.001 6885.219    0.004 agent.py:236(counterfact2)
        192082198/23527516  835.182    0.000 6685.704    0.000 module.py:866(_call_impl)
               15708597  199.659    0.000 6001.948    0.000 container.py:117(forward)
                7818919   65.003    0.000 5710.319    0.001 optimizer.py:84(wrapper)
                1955418  208.678    0.000 5698.321    0.003 agent.py:54(_learn)
               13687462   39.248    0.000 5561.081    0.000 network.py:24(forward)
                7818919   34.715    0.000 5417.458    0.001 grad_mode.py:24(decorate_context)
                7818919  236.379    0.000 5308.122    0.001 adam.py:55(step)
                1955418  203.811    0.000 5244.676    0.003 agent.py:202(_learn)
              194243016  943.172    0.000 4983.732    0.000 layers.py:736(check)
                1955419  316.320    0.000 4888.306    0.002 layers.py:685(update)
                7818919 1113.458    0.000 4811.824    0.001 _functional.py:53(adam)
                1955418 3431.096    0.002 3901.000    0.002 replaybuffer.py:85(sample_data)
                7818919   31.701    0.000 3868.830    0.000 tensor.py:195(backward)
                7818919   31.272    0.000 3835.853    0.000 __init__.py:68(backward)
                1955418   58.539    0.000 3692.116    0.002 agent.py:117(_learn)
                7818919 3648.683    0.000 3648.683    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1955418 2966.525    0.002 3581.061    0.002 replaybuffer.py:22(sample_data)
               34447763 3573.918    0.000 3573.918    0.000 {built-in method tensor}
               30102534   18.639    0.000 3467.433    0.000 game.py:37(board)
                1955418   33.325    0.000 3342.642    0.002 simulator.py:50(learn)
                1955418  207.987    0.000 3309.317    0.002 simulator.py:23(learn)
                1955418 2716.575    0.001 3308.139    0.002 replaybuffer.py:52(sample_data)
               39108370 1703.897    0.000 2842.893    0.000 layer.py:151(update)
                3850158   99.899    0.000 2572.123    0.001 agent.py:49(__call__)
               33438329   81.917    0.000 2403.089    0.000 conv.py:398(forward)
               33438329   51.482    0.000 2282.668    0.000 conv.py:390(_conv_forward)
               33438329 2231.186    0.000 2231.186    0.000 {built-in method conv2d}
                1955418  614.199    0.000 1834.555    0.001 agent.py:88(interveen)
              194243016  315.194    0.000 1751.532    0.000 layers.py:730(isFree)
                1955418 1121.346    0.001 1523.182    0.001 replaybuffer.py:58(CF_save_data)
               37151550   81.749    0.000 1518.233    0.000 linear.py:93(forward)
                1955418  991.652    0.001 1495.635    0.001 agent.py:67(modify)
             1275879443 1218.597    0.000 1436.338    0.000 layer.py:95(isFree)
               37151550   33.289    0.000 1394.368    0.000 functional.py:1737(linear)
               37151550 1353.054    0.000 1353.054    0.000 {built-in method torch._C._nn.linear}
               33233382 1294.644    0.000 1294.644    0.000 {built-in method cat}
                3283061   38.397    0.000 1292.085    0.000 layers.py:741(restart)
                1955418  644.892    0.000 1153.389    0.001 replaybuffer.py:28(teleporter_save_data)
             4053826707  762.800    0.000 1100.604    0.000 enum.py:646(__hash__)
              132913372  938.377    0.000  938.377    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              194214258  217.175    0.000  921.691    0.000 {built-in method builtins.any}
                3283061   18.686    0.000  920.917    0.000 level.py:8(__init__)
                1952666   35.084    0.000  912.196    0.000 agent.py:171(__call__)
               54881282   49.050    0.000  875.344    0.000 activation.py:713(forward)
                7818919  156.771    0.000  864.613    0.000 optimizer.py:189(zero_grad)
                1955418   33.721    0.000  851.831    0.000 agent.py:112(__call__)
               80906370  828.227    0.000  828.227    0.000 {built-in method clone}
               54881282   50.864    0.000  826.294    0.000 functional.py:1364(leaky_relu)
              132913372  823.516    0.000  823.516    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              194243016  599.906    0.000  788.852    0.000 layers.py:78(check)
              195541900   97.354    0.000  775.004    0.000 {built-in method builtins.all}
                5805576   38.182    0.000  769.055    0.000 agent.py:59(modify_board)
                3283061  149.296    0.000  766.761    0.000 levels.py:199(generate)
               54881282  765.442    0.000  765.442    0.000 {built-in method torch._C._nn.leaky_relu}
              194243016  476.242    0.000  724.789    0.000 layers.py:287(check)
             2114847229  578.802    0.000  704.516    0.000 layers.py:701(<genexpr>)
              988022433  271.830    0.000  703.543    0.000 layers.py:691(<genexpr>)
                7826711  696.255    0.000  696.255    0.000 {built-in method torch._C._nn.one_hot}
              194243016  409.618    0.000  650.798    0.000 layers.py:247(check)
              748595156  649.893    0.000  649.893    0.000 layer.py:146(elements)
                2021135    8.826    0.000  607.998    0.000 simulator.py:20(boardforward)
                1955418  480.606    0.000  574.259    0.000 replaybuffer.py:91(simulator_save_data)
               66456686  553.184    0.000  553.184    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                6566122   54.540    0.000  508.915    0.000 level.py:41(notUsed)
               43995551  497.633    0.000  497.633    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              194243016  392.564    0.000  489.822    0.000 layers.py:63(check)
             4897623035  485.023    0.000  485.023    0.000 layer.py:91(positions)
               12432376  186.215    0.000  483.774    0.000 random.py:315(sample)
               66456686  479.800    0.000  479.800    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                1955418   33.369    0.000  462.883    0.000 replaybuffer.py:18(stacker)
                1952666   33.371    0.000  446.266    0.000 replaybuffer.py:48(stacker)
               66456686  443.136    0.000  443.136    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               66456686  441.876    0.000  441.876    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
              465196892  326.617    0.000  407.800    0.000 tensor.py:906(grad)
        5156267702/5156267698  354.296    0.000  393.332    0.000 {built-in method builtins.len}
              195541900  263.356    0.000  389.406    0.000 layers.py:114(isDone)
               10482638  359.479    0.000  359.479    0.000 {built-in method nonzero}
                7818919   10.975    0.000  349.811    0.000 loss.py:527(forward)
              194243016  222.877    0.000  345.093    0.000 layers.py:274(check)
                7818919   31.894    0.000  338.836    0.000 functional.py:2898(mse_loss)
             4053849250  337.808    0.000  337.808    0.000 {built-in method builtins.hash}
               66456686  329.611    0.000  329.611    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              194243016  203.876    0.000  323.711    0.000 layers.py:314(check)
                1955417   27.251    0.000  322.872    0.000 replaybuffer.py:81(stacker)
               32830610   43.710    0.000  321.282    0.000 layer.py:69(restart)
                1955418  182.126    0.000  300.717    0.000 collector.py:46(collect)
              335476954  246.915    0.000  299.836    0.000 layer.py:130(add)
              194243016  198.844    0.000  287.848    0.000 layers.py:49(check)
                3850158   97.332    0.000  268.482    0.000 exploration.py:53(softmaxer)
                1955418   42.188    0.000  233.603    0.000 agent.py:277(counterfact_check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9511604: <CFv2TESTCAU4cf2_0> in cluster <dcc> Done

Job <CFv2TESTCAU4cf2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon Apr 12 20:13:41 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Mon Apr 12 21:11:01 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 12 21:11:01 2021
Terminated at Tue Apr 13 13:06:16 2021
Results reported at Tue Apr 13 13:06:16 2021

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

    CPU time :                                   57170.89 sec.
    Max Memory :                                 8478 MB
    Average Memory :                             6014.37 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               7906.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57314 sec.
    Turnaround time :                            60755 sec.

The output (if any) is above this job summary.

