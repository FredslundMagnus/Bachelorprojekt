
# Parameters

    Name :                      NOBUGcausal3_CFagent_convert0-0
    Main :                      CFagent
    Level :                     Levels.Causal3
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


      34057983599 function calls (33838386860 primitive calls) in 57320.41 seconds

##    Ordered by: cumulative time
   List reduced from 490 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 57320.414 57320.414 {built-in method builtins.exec}
                      1    4.585    4.585 57320.414 57320.414 <string>:1(<module>)
                      1  171.714  171.714 57315.829 57315.829 main.py:96(CFagent)
                7041228   27.008    0.000 21164.540    0.003 agent.py:28(learn)
                7041214  528.132    0.000 17608.543    0.003 learner.py:42(Qlearn)
                2347076   11.531    0.000 9161.864    0.004 game.py:36(step)
        245718208/26123160 1017.722    0.000 9097.998    0.000 module.py:866(_call_impl)
                2347076   15.354    0.000 8623.540    0.004 layers.py:594(step)
               19081946   51.741    0.000 8540.594    0.000 network.py:24(forward)
               19081946  264.735    0.000 8371.262    0.000 container.py:117(forward)
                2347076  252.424    0.000 8176.261    0.003 agent.py:53(_learn)
                2347076  249.402    0.000 7573.433    0.003 agent.py:191(_learn)
                7041214   61.939    0.000 7418.921    0.001 optimizer.py:84(wrapper)
                7041214   29.546    0.000 7132.796    0.001 grad_mode.py:24(decorate_context)
                7041214  209.350    0.000 7037.579    0.001 adam.py:55(step)
                7041214 1443.059    0.000 6599.421    0.001 _functional.py:53(adam)
                2347076  611.487    0.000 6497.421    0.003 agent.py:199(counterfact)
                2347076  204.666    0.000 5753.545    0.002 layers.py:18(step)
              234707600  279.646    0.000 5529.355    0.000 layer.py:82(move)
                2347076 2921.377    0.001 5479.736    0.002 replaybuffer.py:28(teleporter_save_data)
                2347076   70.994    0.000 5371.004    0.002 agent.py:114(_learn)
                7041214   30.667    0.000 4438.246    0.001 tensor.py:195(backward)
                7041214   27.208    0.000 4406.573    0.001 __init__.py:68(backward)
                6019434  166.396    0.000 4378.450    0.001 agent.py:48(__call__)
                7041214 4221.892    0.001 4221.892    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2347076 2275.760    0.001 3969.123    0.002 agent.py:85(interveen)
                2347076 2764.396    0.001 3619.956    0.002 replaybuffer.py:22(sample_data)
              234707600  499.674    0.000 3100.367    0.000 layers.py:611(check)
               38163892   96.711    0.000 3037.382    0.000 conv.py:398(forward)
                2347076 2233.162    0.001 2978.783    0.001 replaybuffer.py:49(sample_data)
               32733411 2933.700    0.000 2933.700    0.000 {built-in method tensor}
               38163892   50.059    0.000 2897.766    0.000 conv.py:390(_conv_forward)
               38163892 2847.708    0.000 2847.708    0.000 {built-in method conv2d}
                2347077  251.091    0.000 2832.875    0.001 layers.py:565(update)
               27236483   18.797    0.000 2773.724    0.000 game.py:32(board)
               52551686  106.084    0.000 2414.287    0.000 linear.py:93(forward)
              175873525 2290.047    0.000 2290.047    0.000 {built-in method clone}
               37553224 1259.160    0.000 2257.010    0.000 layer.py:143(NoRock_update)
               52551686   44.147    0.000 2253.987    0.000 functional.py:1737(linear)
               52551686 2199.177    0.000 2199.177    0.000 {built-in method torch._C._nn.linear}
                1327160   14.959    0.000 2177.722    0.002 agent.py:167(choose_action)
              234701479  322.923    0.000 1897.286    0.000 layers.py:605(isFree)
                2347076 1088.583    0.000 1810.757    0.001 agent.py:66(modify)
             1636480998 1331.322    0.000 1574.363    0.000 layer.py:79(isFree)
               34184276 1393.529    0.000 1393.529    0.000 {built-in method cat}
              131435976 1350.085    0.000 1350.085    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               71633632   58.122    0.000 1337.486    0.000 activation.py:713(forward)
               71633632   59.529    0.000 1279.364    0.000 functional.py:1364(leaky_relu)
                8366510   57.093    0.000 1216.508    0.000 agent.py:58(modify_board)
               71633632 1208.375    0.000 1208.375    0.000 {built-in method torch._C._nn.leaky_relu}
                2347062   44.307    0.000 1190.089    0.001 agent.py:163(__call__)
              131435976 1185.234    0.000 1185.234    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                2347076   42.997    0.000 1124.710    0.000 agent.py:109(__call__)
                7041214  164.828    0.000 1024.023    0.000 optimizer.py:189(zero_grad)
                8366510  777.299    0.000  777.299    0.000 {built-in method torch._C._nn.one_hot}
             3134290702  533.432    0.000  771.346    0.000 enum.py:646(__hash__)
              234707600  477.497    0.000  764.816    0.000 layers.py:303(check)
               65717988  733.667    0.000  733.667    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              234707600  419.647    0.000  704.882    0.000 layers.py:262(check)
                2347076   56.677    0.000  689.330    0.000 replaybuffer.py:18(stacker)
              234707700   78.231    0.000  686.643    0.000 {built-in method builtins.all}
                2438563   24.762    0.000  679.859    0.000 layers.py:615(restart)
               65717988  644.753    0.000  644.753    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              897827724  214.312    0.000  635.469    0.000 layers.py:571(<genexpr>)
               65717988  613.098    0.000  613.098    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                2347076  247.598    0.000  612.263    0.000 replaybuffer.py:55(CF_save_data)
               65717988  609.439    0.000  609.439    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2347062   48.221    0.000  587.188    0.000 replaybuffer.py:45(stacker)
              759363138  585.905    0.000  585.905    0.000 layer.py:122(elements)
              186587097  574.391    0.000  574.391    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                1327160  502.109    0.000  569.488    0.000 agent.py:178(convert_values)
                2347076  293.203    0.000  481.405    0.000 collector.py:54(collect)
               65717988  466.692    0.000  466.692    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                2438563   12.700    0.000  461.296    0.000 level.py:8(__init__)
                6019434  165.151    0.000  453.903    0.000 exploration.py:53(softmaxer)
              234707600  257.592    0.000  405.182    0.000 layers.py:329(check)
              460026000  306.375    0.000  377.758    0.000 tensor.py:906(grad)
              234707700  251.238    0.000  372.338    0.000 layers.py:111(isDone)
                2438563   48.935    0.000  368.386    0.000 levels.py:164(generate)
              234707600  231.337    0.000  364.675    0.000 layers.py:288(check)
                9571278  135.266    0.000  361.382    0.000 random.py:315(sample)
             4150119962  348.909    0.000  348.909    0.000 layer.py:75(positions)
        4532480210/4532480207  302.042    0.000  347.290    0.000 {built-in method builtins.len}
                7041214   10.339    0.000  342.525    0.000 loss.py:527(forward)
                7041214   28.276    0.000  332.186    0.000 functional.py:2898(mse_loss)
                7041229  312.408    0.000  312.408    0.000 {built-in method nonzero}
              234707600  206.757    0.000  305.800    0.000 layers.py:47(check)
                4877126   41.936    0.000  255.823    0.000 level.py:41(notUsed)
             3134317613  237.919    0.000  237.919    0.000 {built-in method builtins.hash}
                7041214  218.230    0.000  218.230    0.000 {built-in method torch._C._nn.mse_loss}
               38163892   25.428    0.000  217.286    0.000 flatten.py:39(forward)
               14082456  200.648    0.000  200.648    0.000 {built-in method sum}
                7042049  198.755    0.000  198.755    0.000 {built-in method max}
               10715450   15.903    0.000  194.434    0.000 tensor.py:525(__rsub__)
               38163892  191.858    0.000  191.858    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              305770774  127.970    0.000  187.816    0.000 random.py:250(_randbelow_with_getrandbits)
               19508504   24.970    0.000  187.502    0.000 layer.py:56(restart)
              343145415  133.123    0.000  183.526    0.000 layer.py:106(add)
              219941803  120.445    0.000  177.738    0.000 layer.py:102(remove)
               10715450  175.890    0.000  175.890    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9494237: <NOBUGcausal3_CFagent_convert0_0> in cluster <dcc> Done

Job <NOBUGcausal3_CFagent_convert0_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sun Apr  4 02:59:52 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sun Apr  4 02:59:53 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr  4 02:59:53 2021
Terminated at Sun Apr  4 18:55:29 2021
Results reported at Sun Apr  4 18:55:29 2021

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

    CPU time :                                   57169.62 sec.
    Max Memory :                                 7760 MB
    Average Memory :                             5560.34 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               8624.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   57363 sec.
    Turnaround time :                            57337 sec.

The output (if any) is above this job summary.

