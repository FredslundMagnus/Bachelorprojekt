
# Parameters

    Name :                      NOBUGcausal4_teleport-0
    Main :                      teleport
    Level :                     Levels.Causal4
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


      54489253300 function calls (54265254229 primitive calls) in 57314.67 seconds

##    Ordered by: cumulative time
   List reduced from 478 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57314.665 57314.665 {built-in method builtins.exec}
                      1    1.935    1.935 57314.665 57314.665 <string>:1(<module>)
                      1  186.560  186.560 57312.730 57312.730 main.py:42(teleport)
                4017345   17.409    0.000 19976.334    0.005 game.py:36(step)
                8034690   28.235    0.000 19063.459    0.002 agent.py:28(learn)
                4017345   22.790    0.000 19057.198    0.005 layers.py:594(step)
                8034690  502.347    0.000 15766.750    0.002 learner.py:42(Qlearn)
                4017345  336.096    0.000 13383.210    0.003 layers.py:18(step)
              401734500  929.656    0.000 13010.576    0.000 layer.py:82(move)
                4017345  436.932    0.000 11569.628    0.003 agent.py:53(_learn)
        252038370/28040310 1040.081    0.000 8402.790    0.000 module.py:866(_call_impl)
              401734500 1293.108    0.000 8047.775    0.000 layers.py:611(check)
               20005620   59.117    0.000 7803.389    0.000 network.py:24(forward)
               20005620  245.756    0.000 7613.888    0.000 container.py:117(forward)
                4017345  120.423    0.000 7448.298    0.002 agent.py:114(_learn)
                8034690   65.628    0.000 6084.682    0.001 optimizer.py:84(wrapper)
                8034690   34.910    0.000 5784.352    0.001 grad_mode.py:24(decorate_context)
                8034690  231.899    0.000 5671.119    0.001 adam.py:55(step)
                4017346  438.881    0.000 5621.607    0.001 layers.py:565(update)
                7953585  191.060    0.000 5183.042    0.001 agent.py:48(__call__)
                8034690 1210.261    0.000 5157.169    0.001 _functional.py:53(adam)
                4017345 3479.845    0.001 4849.379    0.001 replaybuffer.py:22(sample_data)
                4017345 1617.147    0.000 4127.398    0.001 agent.py:85(interveen)
                8034690   33.378    0.000 4063.330    0.001 tensor.py:195(backward)
                8034690   32.135    0.000 4028.659    0.001 __init__.py:68(backward)
                8034690 3833.165    0.000 3833.165    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4017345 2126.310    0.001 3684.556    0.001 replaybuffer.py:28(teleporter_save_data)
              401734500  706.334    0.000 3472.109    0.000 layers.py:605(isFree)
               40011240   95.674    0.000 2862.378    0.000 conv.py:398(forward)
             3152838911 2245.120    0.000 2765.776    0.000 layer.py:79(isFree)
               40011240   55.829    0.000 2722.649    0.000 conv.py:390(_conv_forward)
               40173460 1591.491    0.000 2701.172    0.000 layer.py:127(update)
               40011240 2666.820    0.000 2666.820    0.000 {built-in method conv2d}
                4017345 1529.483    0.000 2594.530    0.001 agent.py:66(modify)
               51982170  113.382    0.000 2098.922    0.000 linear.py:93(forward)
               51982170   48.335    0.000 1931.290    0.000 functional.py:1737(linear)
               51982170 1872.315    0.000 1872.315    0.000 {built-in method torch._C._nn.linear}
             6496848675 1232.312    0.000 1737.355    0.000 enum.py:646(__hash__)
                4017345   58.415    0.000 1680.790    0.000 agent.py:109(__call__)
               11970930   76.331    0.000 1565.520    0.000 agent.py:58(modify_board)
              401734500  861.213    0.000 1365.739    0.000 layers.py:303(check)
              141748872 1348.998    0.000 1348.998    0.000 {built-in method clone}
               17206614 1345.749    0.000 1345.749    0.000 {built-in method tensor}
               36075000 1303.637    0.000 1303.637    0.000 {built-in method cat}
              401734500  792.636    0.000 1296.872    0.000 layers.py:262(check)
                3478706   38.716    0.000 1204.003    0.000 layers.py:615(restart)
              401734500  900.891    0.000 1170.292    0.000 layers.py:76(check)
               71987790   62.814    0.000 1137.333    0.000 activation.py:713(forward)
              401734600  117.894    0.000 1109.559    0.000 {built-in method builtins.all}
                8034690    9.821    0.000 1099.648    0.000 game.py:32(board)
               71987790   65.742    0.000 1074.518    0.000 functional.py:1364(leaky_relu)
                4017345   73.482    0.000 1063.197    0.000 replaybuffer.py:18(stacker)
             1205282810  307.317    0.000 1041.098    0.000 layers.py:571(<genexpr>)
               11970930 1026.266    0.000 1026.266    0.000 {built-in method torch._C._nn.one_hot}
               71987790  996.465    0.000  996.465    0.000 {built-in method torch._C._nn.leaky_relu}
              144624420  985.001    0.000  985.001    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                8034690  164.526    0.000  916.339    0.000 optimizer.py:189(zero_grad)
             9633368834  898.254    0.000  898.254    0.000 layer.py:75(positions)
              144624420  887.815    0.000  887.815    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3478706   18.340    0.000  820.048    0.000 level.py:8(__init__)
              401734500  609.189    0.000  793.717    0.000 layers.py:63(check)
              401734500  483.661    0.000  750.952    0.000 layers.py:329(check)
              401734600  470.879    0.000  699.061    0.000 layers.py:111(isDone)
              401734500  451.358    0.000  696.633    0.000 layers.py:288(check)
             1170631644  692.341    0.000  692.341    0.000 layer.py:122(elements)
                3478706  118.950    0.000  666.660    0.000 levels.py:199(generate)
                4017345  358.286    0.000  608.488    0.000 collector.py:54(collect)
               72312210  586.148    0.000  586.148    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              401734500  386.183    0.000  570.061    0.000 layers.py:47(check)
               72312210  520.522    0.000  520.522    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7953585  189.672    0.000  513.415    0.000 exploration.py:53(softmaxer)
             6496877946  505.049    0.000  505.049    0.000 {built-in method builtins.hash}
               72312210  475.245    0.000  475.245    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               72312210  471.982    0.000  471.982    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              506185524  347.851    0.000  437.406    0.000 tensor.py:906(grad)
                6957412   50.986    0.000  436.490    0.000 level.py:41(notUsed)
        4056653402/4056653400  305.207    0.000  360.678    0.000 {built-in method builtins.len}
               72312210  359.201    0.000  359.201    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                8034690   12.687    0.000  354.149    0.000 loss.py:527(forward)
               10974757  130.674    0.000  347.627    0.000 random.py:315(sample)
                8034690   34.303    0.000  341.462    0.000 functional.py:2898(mse_loss)
               34787060   48.463    0.000  333.548    0.000 layer.py:56(restart)
              153719802  318.871    0.000  318.871    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              545571116  235.377    0.000  318.011    0.000 layer.py:106(add)
             2519856782  272.860    0.000  272.860    0.000 layer.py:183(isBlocking)
               24104070  260.708    0.000  260.708    0.000 {built-in method sum}
              320077202  173.507    0.000  259.672    0.000 layer.py:102(remove)
                8034690  209.298    0.000  209.298    0.000 {built-in method torch._C._nn.mse_loss}
                4017345   17.325    0.000  207.880    0.000 exploration.py:47(epsilonGreedy)
              139148240  205.462    0.000  205.462    0.000 level.py:32(inverse)
              277817374  133.622    0.000  195.494    0.000 random.py:250(_randbelow_with_getrandbits)
               40011240   29.992    0.000  194.807    0.000 flatten.py:39(forward)
                8035886  190.174    0.000  190.174    0.000 {built-in method max}
                3478806   93.305    0.000  188.909    0.000 layers.py:33(reset)
               12052035   17.888    0.000  185.574    0.000 tensor.py:525(__rsub__)
               40011240  164.815    0.000  164.815    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               12052035  164.661    0.000  164.661    0.000 {built-in method rsub}
                7953585  163.024    0.000  163.024    0.000 {built-in method multinomial}
             1906132864  157.635    0.000  157.635    0.000 {method 'append' of 'list' objects}
                8034690   33.505    0.000  156.544    0.000 __init__.py:28(_make_grads)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9494240: <NOBUGcausal4_teleport_0> in cluster <dcc> Done

Job <NOBUGcausal4_teleport_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:52 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:24 2021
Results reported at Sun Apr  4 18:55:24 2021

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

    CPU time :                                   57167.16 sec.
    Max Memory :                                 8136 MB
    Average Memory :                             5482.62 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8248.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57330 sec.
    Turnaround time :                            57332 sec.

The output (if any) is above this job summary.

