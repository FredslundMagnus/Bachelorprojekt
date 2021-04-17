
# Parameters

    Name :                      causal3_CFagent_convert2-0
    Main :                      CFagent
    Level :                     Levels.Causal3
    Hours :                     13.0
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
    Cf convert :                1
    Minutes used :              775 minutes.
    Hours used :                12 hours.

# Profiling


      32780822215 function calls (32566047836 primitive calls) in 46519.58 seconds

##    Ordered by: cumulative time
   List reduced from 489 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 46519.578 46519.578 {built-in method builtins.exec}
                      1    4.671    4.671 46519.578 46519.578 <string>:1(<module>)
                      1  160.280  160.280 46514.907 46514.907 main.py:96(CFagent)
                6956847   25.817    0.000 16046.835    0.002 agent.py:28(learn)
                6956837  406.340    0.000 13014.975    0.002 learner.py:42(Qlearn)
                2318949   10.644    0.000 8858.496    0.004 game.py:36(step)
                2318949   13.166    0.000 8386.974    0.004 layers.py:594(step)
        240400232/25627544  906.447    0.000 7387.780    0.000 module.py:866(_call_impl)
               18670707   46.371    0.000 6905.040    0.000 network.py:24(forward)
               18670707  217.181    0.000 6742.343    0.000 container.py:117(forward)
                2318949  246.397    0.000 6247.372    0.003 agent.py:53(_learn)
                2318949  243.241    0.000 5732.007    0.002 agent.py:189(_learn)
                2318949  203.161    0.000 5640.875    0.002 layers.py:18(step)
              231643635  269.714    0.000 5417.982    0.000 layer.py:82(move)
                2318949  467.033    0.000 5318.799    0.002 agent.py:197(counterfact)
                6956837   53.706    0.000 5074.112    0.001 optimizer.py:84(wrapper)
                6956837   28.922    0.000 4828.866    0.001 grad_mode.py:24(decorate_context)
                6956837  206.432    0.000 4737.192    0.001 adam.py:55(step)
                6956837  994.099    0.000 4305.027    0.001 _functional.py:53(adam)
                2318949   67.785    0.000 4027.426    0.002 agent.py:114(_learn)
                2318949 2040.225    0.001 3564.939    0.002 replaybuffer.py:28(teleporter_save_data)
                5855751  152.121    0.000 3560.050    0.001 agent.py:48(__call__)
                2318949 2675.013    0.001 3448.968    0.001 replaybuffer.py:22(sample_data)
                6956837   27.510    0.000 3401.458    0.000 tensor.py:195(backward)
                6956837   25.203    0.000 3372.988    0.000 __init__.py:68(backward)
                6956837 3219.186    0.000 3219.186    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              231643635  492.335    0.000 3007.433    0.000 layers.py:611(check)
                2318949 1487.693    0.001 2882.451    0.001 agent.py:85(interveen)
                2318949 2161.840    0.001 2837.655    0.001 replaybuffer.py:49(sample_data)
               33325301 2715.927    0.000 2715.927    0.000 {built-in method tensor}
                2318950  238.961    0.000 2711.583    0.001 layers.py:565(update)
               26818611   17.528    0.000 2554.142    0.000 game.py:32(board)
               37341414   80.052    0.000 2508.849    0.000 conv.py:398(forward)
               37341414   59.385    0.000 2390.160    0.000 conv.py:390(_conv_forward)
               37341414 2330.775    0.000 2330.775    0.000 {built-in method conv2d}
               37103192 1258.340    0.000 2245.269    0.000 layer.py:143(NoRock_update)
              231532898  317.922    0.000 1892.860    0.000 layers.py:605(isFree)
               51374223   97.459    0.000 1886.504    0.000 linear.py:93(forward)
               51374223   40.162    0.000 1738.768    0.000 functional.py:1737(linear)
               51374223 1689.158    0.000 1689.158    0.000 {built-in method torch._C._nn.linear}
             1534378277 1346.901    0.000 1574.939    0.000 layer.py:79(isFree)
                2318949  862.706    0.000 1437.685    0.001 agent.py:66(modify)
              156669557 1425.386    0.000 1425.386    0.000 {built-in method clone}
                1220231   10.606    0.000 1338.893    0.001 agent.py:167(choose_action)
               33683089 1191.810    0.000 1191.810    0.000 {built-in method cat}
               70044930   56.024    0.000 1010.969    0.000 activation.py:713(forward)
                8174700   50.345    0.000  997.362    0.000 agent.py:58(modify_board)
                2318939   40.260    0.000  982.929    0.000 agent.py:163(__call__)
               70044930   54.209    0.000  954.945    0.000 functional.py:1364(leaky_relu)
                2318949   37.734    0.000  933.851    0.000 agent.py:109(__call__)
               70044930  889.605    0.000  889.605    0.000 {built-in method torch._C._nn.leaky_relu}
              129860944  841.438    0.000  841.438    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              129860944  744.752    0.000  744.752    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                6956837  133.472    0.000  737.844    0.000 optimizer.py:189(zero_grad)
              231643635  466.424    0.000  731.735    0.000 layers.py:303(check)
             3085378532  520.030    0.000  726.590    0.000 enum.py:646(__hash__)
                2408891   24.066    0.000  678.567    0.000 layers.py:615(restart)
              231643635  400.801    0.000  668.416    0.000 layers.py:262(check)
                8174700  657.121    0.000  657.121    0.000 {built-in method torch._C._nn.one_hot}
                2318949   53.393    0.000  609.128    0.000 replaybuffer.py:18(stacker)
              231895000   63.654    0.000  599.653    0.000 {built-in method builtins.all}
              712171095  575.682    0.000  575.682    0.000 layer.py:122(elements)
              712395855  164.446    0.000  561.282    0.000 layers.py:571(<genexpr>)
                2318939   50.187    0.000  516.876    0.000 replaybuffer.py:45(stacker)
               64930472  490.875    0.000  490.875    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2318949  195.898    0.000  465.962    0.000 replaybuffer.py:55(CF_save_data)
                2408891   13.692    0.000  458.728    0.000 level.py:8(__init__)
               64930472  435.345    0.000  435.345    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              231643635  253.941    0.000  393.619    0.000 layers.py:329(check)
               64930472  393.507    0.000  393.507    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               64930472  390.033    0.000  390.033    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              231895000  257.542    0.000  374.791    0.000 layers.py:111(isDone)
                2408891   49.002    0.000  367.728    0.000 levels.py:164(generate)
              231643635  236.245    0.000  361.849    0.000 layers.py:288(check)
                9455680  135.185    0.000  360.627    0.000 random.py:315(sample)
                5855751  132.770    0.000  356.880    0.000 exploration.py:53(softmaxer)
              454513388  284.422    0.000  351.432    0.000 tensor.py:906(grad)
             4011051966  345.421    0.000  345.421    0.000 layer.py:75(positions)
                2318949  197.875    0.000  333.796    0.000 collector.py:54(collect)
        4486798570/4486798567  284.677    0.000  325.015    0.000 {built-in method builtins.len}
              167163196  307.038    0.000  307.038    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              231643635  205.929    0.000  302.217    0.000 layers.py:47(check)
               64930472  288.680    0.000  288.680    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                6956837   12.053    0.000  281.498    0.000 loss.py:527(forward)
                6956837   25.377    0.000  269.445    0.000 functional.py:2898(mse_loss)
                3539180   18.700    0.000  264.529    0.000 exploration.py:47(epsilonGreedy)
                6956848  260.232    0.000  260.232    0.000 {built-in method nonzero}
                4817782   40.766    0.000  254.965    0.000 level.py:41(notUsed)
             3085405107  206.565    0.000  206.565    0.000 {built-in method builtins.hash}
               19271128   23.423    0.000  189.284    0.000 layer.py:56(restart)
              319642054  133.486    0.000  184.052    0.000 layer.py:106(add)
              290867182  125.001    0.000  183.607    0.000 random.py:250(_randbelow_with_getrandbits)
              198018306  126.595    0.000  182.526    0.000 layer.py:102(remove)
               37341414   31.608    0.000  173.525    0.000 flatten.py:39(forward)
                6956837  166.695    0.000  166.695    0.000 {built-in method torch._C._nn.mse_loss}
                6957775  152.853    0.000  152.853    0.000 {built-in method max}
               13913694  142.640    0.000  142.640    0.000 {built-in method sum}
               37103192  142.481    0.000  142.481    0.000 layer.py:154(<listcomp>)
               37341414  141.916    0.000  141.916    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1855856   62.951    0.000  137.235    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-5>
Subject: Job 9493321: <causal3_CFagent_convert2_0> in cluster <dcc> Done

Job <causal3_CFagent_convert2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri Apr  2 22:10:09 2021
Job was executed on host(s) <n-62-20-5>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Apr  3 11:06:50 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Apr  3 11:06:50 2021
Terminated at Sun Apr  4 00:02:17 2021
Results reported at Sun Apr  4 00:02:17 2021

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

    CPU time :                                   46394.25 sec.
    Max Memory :                                 7869 MB
    Average Memory :                             5707.51 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8515.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   46529 sec.
    Turnaround time :                            93128 sec.

The output (if any) is above this job summary.

