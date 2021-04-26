
# Parameters

    Name :                      SuperLevel2_teleport-2
    Main :                      teleport
    Level :                     Levels.SuperLevel2
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


      94281579931 function calls (94043955856 primitive calls) in 86106.11 seconds

##    Ordered by: cumulative time
   List reduced from 483 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86106.114 86106.114 {built-in method builtins.exec}
                      1    1.442    1.442 86106.114 86106.114 <string>:1(<module>)
                      1  188.819  188.819 86104.672 86104.672 main.py:45(teleport)
                4268349   18.103    0.000 30979.316    0.007 game.py:41(step)
                8536698   30.596    0.000 30662.593    0.004 agent.py:29(learn)
                4268349   21.947    0.000 29825.241    0.007 layers.py:718(step)
                8536698  727.725    0.000 26313.475    0.003 learner.py:42(Qlearn)
                4268349  409.079    0.000 22190.448    0.005 layers.py:17(step)
              426834900 1500.397    0.000 21742.571    0.000 layer.py:98(move)
                4268349  141.318    0.000 18421.310    0.004 agent.py:54(_learn)
              426834900 2493.484    0.000 15576.605    0.000 layers.py:735(check)
                4268349  116.138    0.000 12193.334    0.003 agent.py:117(_learn)
        267384467/29761403 1093.129    0.000 11908.376    0.000 module.py:715(_call_impl)
                8536698   52.343    0.000 11318.194    0.001 grad_mode.py:23(decorate_context)
                8536698  298.513    0.000 11163.774    0.001 adam.py:55(step)
               21224705   57.145    0.000 11154.170    0.001 network.py:27(forward)
               21224705  288.158    0.000 10970.762    0.001 container.py:115(forward)
                8536698 2053.424    0.000 9624.434    0.001 functional.py:53(adam)
                4268350  596.283    0.000 7585.536    0.002 layers.py:684(update)
                8419658  185.640    0.000 7208.649    0.001 agent.py:49(__call__)
                8536698   53.542    0.000 5951.437    0.001 tensor.py:181(backward)
                4268349 2389.285    0.001 5932.730    0.001 agent.py:88(interveen)
                8536698   32.860    0.000 5897.895    0.001 __init__.py:68(backward)
                8536698 5635.440    0.001 5635.440    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4268349 3044.932    0.001 5041.801    0.001 replaybuffer.py:22(sample_data)
                4268349 2524.121    0.001 4820.246    0.001 agent.py:67(modify)
                4268349 2278.923    0.001 4497.433    0.001 replaybuffer.py:28(teleporter_save_data)
               42449410   74.585    0.000 3931.002    0.000 conv.py:422(forward)
               42449410   79.372    0.000 3828.547    0.000 conv.py:414(_conv_forward)
              426834900  774.587    0.000 3735.289    0.000 layers.py:729(isFree)
               42449410 3734.956    0.000 3734.956    0.000 {built-in method conv2d}
               55137417  131.033    0.000 3573.585    0.000 linear.py:92(forward)
              426834900 2478.118    0.000 3447.569    0.000 layers.py:471(check)
               55137417  228.618    0.000 3388.231    0.000 functional.py:1669(linear)
               46951850 1780.341    0.000 2996.610    0.000 layer.py:151(update)
             3530022912 2299.659    0.000 2960.702    0.000 layer.py:95(isFree)
            11553495603 2059.360    0.000 2958.349    0.000 enum.py:646(__hash__)
             1193586216  756.921    0.000 2862.412    0.000 {built-in method builtins.any}
               55137417 2432.411    0.000 2432.411    0.000 {built-in method addmm}
              537812028 1482.854    0.000 2326.932    0.000 tensor.py:933(grad)
                4268349   57.318    0.000 2292.959    0.001 agent.py:112(__call__)
                8536698  221.813    0.000 2269.610    0.000 optimizer.py:167(zero_grad)
              426834900 1528.472    0.000 2180.631    0.000 layers.py:77(check)
               12688007   95.994    0.000 2145.107    0.000 agent.py:59(modify_board)
               34029752 2096.407    0.000 2096.407    0.000 {built-in method cat}
              153660564 2005.274    0.000 2005.274    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              426834900 1175.134    0.000 1973.151    0.000 layers.py:246(check)
              426834900 1068.316    0.000 1863.454    0.000 layers.py:286(check)
              118287623 1810.212    0.000 1810.212    0.000 {built-in method clone}
              153660564 1707.768    0.000 1707.768    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4268349   72.810    0.000 1690.723    0.000 replaybuffer.py:18(stacker)
             5060578068 1401.878    0.000 1683.254    0.000 layers.py:700(<genexpr>)
               76362122   68.556    0.000 1663.591    0.000 activation.py:713(forward)
               18263209 1653.072    0.000 1653.072    0.000 {built-in method tensor}
               76362122  105.329    0.000 1595.036    0.000 functional.py:1292(leaky_relu)
               76362122 1479.760    0.000 1479.760    0.000 {built-in method torch._C._nn.leaky_relu}
               12688007 1338.824    0.000 1338.824    0.000 {built-in method torch._C._nn.one_hot}
                8536698   12.186    0.000 1304.381    0.000 game.py:37(board)
            12856486737 1266.037    0.000 1266.037    0.000 layer.py:91(positions)
               29881587  168.032    0.000 1167.274    0.000 tensor.py:21(wrapped)
              699660563  389.878    0.000 1144.796    0.000 overrides.py:1070(has_torch_function)
               76830282 1104.506    0.000 1104.506    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                5120161   58.516    0.000 1078.703    0.000 layers.py:740(restart)
                4268349  632.330    0.000 1063.058    0.000 collector.py:46(collect)
               76830282 1004.008    0.000 1004.008    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               76830282  910.953    0.000  910.953    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
            11553526674  898.995    0.000  898.995    0.000 {built-in method builtins.hash}
               76830282  813.100    0.000  813.100    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                8419658  274.000    0.000  767.478    0.000 exploration.py:53(softmaxer)
              426834900  494.593    0.000  763.058    0.000 layers.py:313(check)
              426834900  456.535    0.000  711.580    0.000 layers.py:273(check)
             1421528827  706.619    0.000  706.619    0.000 layer.py:146(elements)
               76830282  642.054    0.000  642.054    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              456716587  145.860    0.000  638.320    0.000 {built-in method builtins.all}
              426834900  419.748    0.000  608.061    0.000 layers.py:62(check)
              130975630  596.782    0.000  596.782    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              426834900  393.771    0.000  592.442    0.000 layers.py:48(check)
        6325159701/6325159699  438.665    0.000  573.272    0.000 {built-in method builtins.len}
                5120161   27.378    0.000  531.824    0.000 level.py:8(__init__)
              410906672  203.616    0.000  524.268    0.000 random.py:285(choice)
             1280505900  310.319    0.000  523.637    0.000 layers.py:690(<genexpr>)
                8536698   12.502    0.000  507.733    0.000 loss.py:445(forward)
                8536698   52.031    0.000  495.231    0.000 functional.py:2637(mse_loss)
               21341745  494.808    0.000  494.808    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              426834900  327.208    0.000  474.150    0.000 layers.py:23(check)
               55137417  471.966    0.000  471.966    0.000 {method 't' of 'torch._C._TensorBase' objects}
               56321771   66.416    0.000  470.172    0.000 layer.py:69(restart)
               25610094  428.246    0.000  428.246    0.000 {built-in method sum}
             5167248437  427.024    0.000  427.024    0.000 {method 'random' of '_random.Random' objects}
             1484339289  331.897    0.000  416.637    0.000 overrides.py:1083(<genexpr>)
              624377559  286.309    0.000  412.154    0.000 random.py:250(_randbelow_with_getrandbits)
             2897339966  379.892    0.000  379.892    0.000 layer.py:203(isBlocking)
              664558270  281.371    0.000  378.505    0.000 layer.py:130(add)
               42449410   40.420    0.000  310.522    0.000 flatten.py:39(forward)
                8536698  310.219    0.000  310.219    0.000 {built-in method torch._C._nn.mse_loss}
                4268349  111.007    0.000  298.241    0.000 random.py:315(sample)
              352225278  193.328    0.000  295.095    0.000 layer.py:126(remove)
                5120261  131.434    0.000  278.764    0.000 layers.py:36(reset)
                5120161  166.625    0.000  277.331    0.000 levels.py:353(generate)
                8537965  273.383    0.000  273.383    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550913: <SuperLevel2_teleport_2> in cluster <dcc> Done

Job <SuperLevel2_teleport_2> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:50 2021
Job was executed on host(s) <n-62-11-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Apr 24 18:06:15 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr 24 18:06:15 2021
Terminated at Sun Apr 25 18:01:25 2021
Results reported at Sun Apr 25 18:01:25 2021

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

    CPU time :                                   85893.59 sec.
    Max Memory :                                 2675 MB
    Average Memory :                             2672.45 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13709.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86110 sec.
    Turnaround time :                            437975 sec.

The output (if any) is above this job summary.

