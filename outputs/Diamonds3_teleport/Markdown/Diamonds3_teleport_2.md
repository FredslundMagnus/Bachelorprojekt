
# Parameters

    Name :                      Diamonds3_teleport-2
    Main :                      teleport
    Level :                     Levels.Causal6
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
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      73825955464 function calls (73621153389 primitive calls) in 86104.96 seconds

##    Ordered by: cumulative time
   List reduced from 473 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86104.956 86104.956 {built-in method builtins.exec}
                      1    1.622    1.622 86104.956 86104.956 <string>:1(<module>)
                      1  178.073  178.073 86103.334 86103.334 main.py:45(teleport)
                7314760   27.600    0.000 27587.369    0.004 agent.py:29(learn)
                7314760  647.603    0.000 23679.499    0.003 learner.py:42(Qlearn)
                3657380   15.664    0.000 22193.806    0.006 game.py:41(step)
                3657380   20.830    0.000 21281.759    0.006 layers.py:718(step)
                3657380  126.886    0.000 16570.570    0.005 agent.py:54(_learn)
                3657380 6956.860    0.002 13430.213    0.004 replaybuffer.py:28(teleporter_save_data)
                3657380  299.500    0.000 11309.206    0.003 layers.py:17(step)
                3657380  105.638    0.000 10973.888    0.003 agent.py:117(_learn)
              365738000  648.113    0.000 10972.417    0.000 layer.py:98(move)
        230401706/25600642  989.827    0.000 10711.557    0.000 module.py:715(_call_impl)
                7314760   45.864    0.000 10208.502    0.001 grad_mode.py:23(decorate_context)
                7314760  260.495    0.000 10073.384    0.001 adam.py:55(step)
                3657380 6792.123    0.002 10057.606    0.003 agent.py:88(interveen)
               18285882   51.562    0.000 10034.502    0.001 network.py:27(forward)
                3657381  574.110    0.000 9925.767    0.003 layers.py:684(update)
               18285882  263.178    0.000 9867.247    0.001 container.py:115(forward)
                7314760 1837.395    0.000 8659.642    0.001 functional.py:53(adam)
              365738000 1384.493    0.000 7113.152    0.000 layers.py:735(check)
                7313742  176.300    0.000 6551.007    0.001 agent.py:49(__call__)
                7314760   46.122    0.000 5349.113    0.001 tensor.py:181(backward)
                7314760   29.791    0.000 5302.991    0.001 __init__.py:68(backward)
              327379460 5069.174    0.000 5069.174    0.000 {built-in method clone}
                7314760 5062.856    0.001 5062.856    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3657380 2792.696    0.001 4651.241    0.001 replaybuffer.py:22(sample_data)
                3657380 2464.963    0.001 4522.600    0.001 agent.py:67(modify)
                8277083   85.523    0.000 4103.098    0.000 layers.py:740(restart)
               36571764   68.868    0.000 3552.893    0.000 conv.py:422(forward)
               36571764   79.408    0.000 3458.017    0.000 conv.py:414(_conv_forward)
                8277083   38.950    0.000 3374.715    0.000 level.py:8(__init__)
               36571764 3364.652    0.000 3364.652    0.000 {built-in method conv2d}
               47542886  115.613    0.000 3186.079    0.000 linear.py:92(forward)
               47542886  196.144    0.000 3017.319    0.000 functional.py:1669(linear)
                8277083  121.467    0.000 2982.771    0.000 levels.py:288(generate)
               49664103  486.297    0.000 2729.614    0.000 level.py:41(notUsed)
              365738000  650.885    0.000 2562.264    0.000 layers.py:729(isFree)
             8114872426 1546.413    0.000 2265.218    0.000 enum.py:646(__hash__)
             1019442107  608.488    0.000 2180.021    0.000 {built-in method builtins.any}
               47542886 2158.699    0.000 2158.699    0.000 {built-in method addmm}
              460829934 1355.769    0.000 2147.010    0.000 tensor.py:933(grad)
               29259048 1196.456    0.000 2101.223    0.000 layer.py:167(NoRock_update)
                3657380   54.485    0.000 2078.427    0.001 agent.py:112(__call__)
                7314760  183.763    0.000 2059.095    0.000 optimizer.py:167(zero_grad)
               10971122   87.223    0.000 1940.116    0.000 agent.py:59(modify_board)
               29258022 1935.964    0.000 1935.964    0.000 {built-in method cat}
             2913918219 1519.228    0.000 1911.378    0.000 layer.py:95(isFree)
              131665680 1806.150    0.000 1806.150    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              365738000 1014.251    0.000 1690.334    0.000 layers.py:424(check)
                3657380   68.031    0.000 1571.458    0.000 replaybuffer.py:18(stacker)
              131665680 1535.298    0.000 1535.298    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              338350582 1518.177    0.000 1518.177    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              391341764  158.701    0.000 1511.230    0.000 {built-in method builtins.all}
               65828768   63.580    0.000 1492.650    0.000 activation.py:713(forward)
               65828768   95.409    0.000 1429.070    0.000 functional.py:1292(leaky_relu)
             1388529860  414.137    0.000 1384.733    0.000 layers.py:690(<genexpr>)
               65828768 1324.406    0.000 1324.406    0.000 {built-in method torch._C._nn.leaky_relu}
               49664103   37.454    0.000 1278.701    0.000 level.py:38(elementsIn)
               15693261 1254.626    0.000 1254.626    0.000 {built-in method tensor}
               10971122 1209.800    0.000 1209.800    0.000 {built-in method torch._C._nn.one_hot}
             3217149153  939.447    0.000 1166.588    0.000 layers.py:700(<genexpr>)
              365738000  700.766    0.000 1136.752    0.000 layers.py:452(check)
              365738000  669.872    0.000 1098.329    0.000 layers.py:437(check)
              599808683  365.170    0.000 1065.418    0.000 overrides.py:1070(has_torch_function)
               25603664  148.186    0.000 1057.124    0.000 tensor.py:21(wrapped)
               65832840  992.024    0.000  992.024    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                3657380  565.524    0.000  953.386    0.000 collector.py:46(collect)
                7314760    9.091    0.000  942.465    0.000 game.py:37(board)
               65832840  899.866    0.000  899.866    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             7990716007  878.936    0.000  878.936    0.000 layer.py:91(positions)
               49664103  402.445    0.000  841.579    0.000 level.py:39(<listcomp>)
               65832840  827.961    0.000  827.961    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               65832840  738.493    0.000  738.493    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
             8114899105  718.810    0.000  718.810    0.000 {built-in method builtins.hash}
                7313742  248.396    0.000  702.142    0.000 exploration.py:53(softmaxer)
              365738100  415.484    0.000  666.986    0.000 layers.py:457(isDone)
               66216664   59.501    0.000  618.578    0.000 layer.py:69(restart)
             2355727798  582.507    0.000  582.507    0.000 level.py:32(inverse)
               65832840  579.362    0.000  579.362    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              365738000  354.022    0.000  547.287    0.000 layers.py:413(check)
             1386857369  540.626    0.000  540.626    0.000 layer.py:146(elements)
              365738000  319.278    0.000  501.245    0.000 layers.py:402(check)
        4233907708/4233907706  358.186    0.000  476.681    0.000 {built-in method builtins.len}
                8277183  223.545    0.000  458.184    0.000 layers.py:36(reset)
                7314760   11.061    0.000  452.969    0.000 loss.py:445(forward)
               18286900  442.575    0.000  442.575    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                7314760   41.135    0.000  441.907    0.000 functional.py:2637(mse_loss)
               47542886  428.073    0.000  428.073    0.000 {method 't' of 'torch._C._TensorBase' objects}
              365738000  283.164    0.000  422.398    0.000 layers.py:23(check)
              668286178  292.948    0.000  411.573    0.000 layer.py:130(add)
             2085884222  405.936    0.000  405.936    0.000 enum.py:352(<genexpr>)
               49664103  249.404    0.000  399.669    0.000 {built-in method _functools.reduce}
             1272763185  318.388    0.000  399.161    0.000 overrides.py:1083(<genexpr>)
               21944280  382.453    0.000  382.453    0.000 {built-in method sum}
                8277083  179.780    0.000  328.510    0.000 level.py:16(<dictcomp>)
             2913918219  317.863    0.000  317.863    0.000 layer.py:203(isBlocking)
              372052453  202.808    0.000  301.585    0.000 layer.py:126(remove)
             3336684795  298.643    0.000  298.643    0.000 {method 'random' of '_random.Random' objects}
                7314760  280.433    0.000  280.433    0.000 {built-in method torch._C._nn.mse_loss}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550904: <Diamonds3_teleport_2> in cluster <dcc> Done

Job <Diamonds3_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:49 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr 23 07:23:06 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr 23 07:23:06 2021
Terminated at Sat Apr 24 07:18:13 2021
Results reported at Sat Apr 24 07:18:13 2021

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

    CPU time :                                   85897.22 sec.
    Max Memory :                                 2676 MB
    Average Memory :                             2673.08 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13708.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86109 sec.
    Turnaround time :                            312984 sec.

The output (if any) is above this job summary.

